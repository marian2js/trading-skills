#!/usr/bin/env python3
"""Compute a conservative position size from risk budget and stop distance."""

from __future__ import annotations

import argparse
import json
import math
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate a conservative position size from account risk inputs."
    )
    parser.add_argument("--account-size", type=float, required=True)
    parser.add_argument("--risk-percent", type=float, default=None)
    parser.add_argument("--risk-amount", type=float, default=None)
    parser.add_argument("--entry", type=float, required=True)
    parser.add_argument("--stop", type=float, required=True)
    parser.add_argument("--slippage", type=float, default=0.0)
    parser.add_argument("--fee-per-unit", type=float, default=0.0)
    parser.add_argument(
        "--contract-multiplier",
        type=float,
        default=1.0,
        help="Use 1 for shares. Set the instrument multiplier for futures or other leveraged products.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def calculate_position_size(
    account_size: float,
    risk_percent: float | None,
    risk_amount: float | None,
    entry: float,
    stop: float,
    slippage: float,
    fee_per_unit: float,
    contract_multiplier: float,
) -> dict:
    if risk_percent is None and risk_amount is None:
        raise ValueError("Provide either --risk-percent or --risk-amount.")
    if risk_percent is not None and risk_percent <= 0:
        raise ValueError("--risk-percent must be positive.")
    if risk_amount is not None and risk_amount <= 0:
        raise ValueError("--risk-amount must be positive.")
    if contract_multiplier <= 0:
        raise ValueError("--contract-multiplier must be positive.")

    stop_distance = abs(entry - stop)
    if stop_distance == 0:
        raise ValueError("Entry and stop cannot be equal.")

    allowed_risk = risk_amount if risk_amount is not None else account_size * (risk_percent / 100.0)
    realized_risk_per_unit = (stop_distance + slippage + fee_per_unit) * contract_multiplier
    size = math.floor(allowed_risk / realized_risk_per_unit)
    if size < 1:
        size = 0

    total_risk = round(size * realized_risk_per_unit, 2)
    risk_fraction = round((total_risk / account_size) * 100, 4) if account_size else None

    caveats = []
    if slippage > 0:
        caveats.append("Result includes user-supplied slippage and may still understate fast-market fills.")
    if contract_multiplier != 1:
        caveats.append("Contract multiplier changes realized exposure materially.")
    if stop_distance / entry < 0.0025:
        caveats.append("Very tight stops can create fragile oversizing in live execution.")
    if size == 0:
        caveats.append("Risk budget is too small for even one unit at the stated stop distance.")

    return {
        "position_size": size,
        "allowed_risk": round(allowed_risk, 2),
        "risk_per_unit": round(realized_risk_per_unit, 4),
        "total_risk": total_risk,
        "percent_of_account_at_risk": risk_fraction,
        "assumptions": {
            "entry": entry,
            "stop": stop,
            "stop_distance": round(stop_distance, 4),
            "slippage": slippage,
            "fee_per_unit": fee_per_unit,
            "contract_multiplier": contract_multiplier,
        },
        "common_mistakes": [
            "Ignoring slippage when the stop is tight.",
            "Using equity-style sizing on products with contract multipliers.",
            "Treating arithmetic size as permission to hold through binary event risk.",
        ],
        "caveats": caveats,
    }


def main() -> int:
    args = parse_args()
    try:
        result = calculate_position_size(
            account_size=args.account_size,
            risk_percent=args.risk_percent,
            risk_amount=args.risk_amount,
            entry=args.entry,
            stop=args.stop,
            slippage=args.slippage,
            fee_per_unit=args.fee_per_unit,
            contract_multiplier=args.contract_multiplier,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Position size: {result['position_size']}")
    print(f"Allowed risk: {result['allowed_risk']}")
    print(f"Risk per unit: {result['risk_per_unit']}")
    print(f"Total risk: {result['total_risk']}")
    print(f"Percent of account at risk: {result['percent_of_account_at_risk']}")
    print("Common mistakes:")
    for item in result["common_mistakes"]:
        print(f"- {item}")
    if result["caveats"]:
        print("Caveats:")
        for caveat in result["caveats"]:
            print(f"- {caveat}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
