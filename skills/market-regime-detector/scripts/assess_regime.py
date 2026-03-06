#!/usr/bin/env python3
"""Conservative market regime classifier from structured observations."""

from __future__ import annotations

import argparse
import json
import sys


VALID_STATES = {
    "trend": {"up", "down", "range", "mixed"},
    "volatility": {"contained", "elevated", "expanding"},
    "breadth": {"broad", "mixed", "narrow", "weak"},
    "event_backdrop": {"quiet", "normal", "heavy"},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assess market regime from manual observations."
    )
    parser.add_argument("--trend", required=True, choices=sorted(VALID_STATES["trend"]))
    parser.add_argument(
        "--volatility", required=True, choices=sorted(VALID_STATES["volatility"])
    )
    parser.add_argument(
        "--breadth", required=True, choices=sorted(VALID_STATES["breadth"])
    )
    parser.add_argument(
        "--event-backdrop",
        required=True,
        choices=sorted(VALID_STATES["event_backdrop"]),
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def classify_regime(trend: str, volatility: str, breadth: str, event_backdrop: str) -> dict:
    caveats = []

    if trend == "up" and breadth == "broad" and volatility == "contained":
        regime = "trending-risk-on"
    elif trend == "up" and breadth in {"mixed", "narrow"}:
        regime = "trending-but-fragile"
        caveats.append("Leadership is not broad enough to treat the uptrend as robust.")
    elif trend == "down" and volatility in {"elevated", "expanding"}:
        regime = "defensive-risk-off"
    elif trend == "range":
        regime = "range-bound"
    else:
        regime = "transition"

    if event_backdrop == "heavy":
        caveats.append("Upcoming event risk reduces confidence in any regime label.")
    if volatility == "expanding":
        caveats.append("Expanding volatility argues for smaller size and wider error bars.")

    return {
        "regime": regime,
        "inputs": {
            "trend": trend,
            "volatility": volatility,
            "breadth": breadth,
            "event_backdrop": event_backdrop,
        },
        "caveats": caveats,
    }


def main() -> int:
    args = parse_args()
    result = classify_regime(
        trend=args.trend,
        volatility=args.volatility,
        breadth=args.breadth,
        event_backdrop=args.event_backdrop,
    )

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Regime: {result['regime']}")
    print("Inputs:")
    for key, value in result["inputs"].items():
        print(f"- {key}: {value}")

    if result["caveats"]:
        print("Caveats:")
        for caveat in result["caveats"]:
            print(f"- {caveat}")
    else:
        print("Caveats:\n- No major caveats beyond normal model simplification.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
