#!/usr/bin/env python3
"""Run a conservative structural check on entry, stop, and target levels."""

from __future__ import annotations

import argparse
import json
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check whether a trade's risk-reward structure is coherent."
    )
    parser.add_argument("--direction", required=True, choices=["long", "short"])
    parser.add_argument("--entry", type=float, required=True)
    parser.add_argument("--stop", type=float, required=True)
    parser.add_argument("--target", type=float, required=True)
    parser.add_argument("--thesis", required=True)
    parser.add_argument("--time-horizon", default="unspecified")
    parser.add_argument("--event-risk", default="none")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    return parser.parse_args()


def analyze_structure(
    direction: str,
    entry: float,
    stop: float,
    target: float,
    thesis: str,
    time_horizon: str,
    event_risk: str,
) -> dict:
    if direction == "long":
        risk = entry - stop
        reward = target - entry
    else:
        risk = stop - entry
        reward = entry - target

    if risk <= 0:
        raise ValueError("Stop placement does not define valid risk for the chosen direction.")
    if reward <= 0:
        raise ValueError("Target placement does not define positive reward for the chosen direction.")

    ratio = round(reward / risk, 2)
    asymmetry = (
        "weak" if ratio < 1.5 else "acceptable" if ratio < 2.5 else "strong"
    )

    structural_flags = []
    if ratio < 1.5:
        structural_flags.append("Reward does not materially compensate for the defined risk.")
    if abs(entry - stop) / entry < 0.003:
        structural_flags.append("Stop may be too tight for normal market noise.")
    if event_risk.lower() not in {"none", "low"}:
        structural_flags.append("Event risk can invalidate the static ratio quickly.")
    if time_horizon == "unspecified":
        structural_flags.append("Time horizon is unspecified, which weakens target plausibility.")

    primary_concern = (
        structural_flags[0]
        if structural_flags
        else "Raw ratio is acceptable, but the target still needs a credible path and invalidation logic."
    )

    return {
        "risk": round(risk, 4),
        "reward": round(reward, 4),
        "risk_reward_ratio": ratio,
        "asymmetry": asymmetry,
        "primary_concern": primary_concern,
        "what_must_be_true": (
            "The thesis must remain intact long enough for the target to be reachable without changing the stop logic."
        ),
        "thesis": thesis,
        "time_horizon": time_horizon,
        "event_risk": event_risk,
        "structural_flags": structural_flags,
    }


def main() -> int:
    args = parse_args()
    try:
        result = analyze_structure(
            direction=args.direction,
            entry=args.entry,
            stop=args.stop,
            target=args.target,
            thesis=args.thesis,
            time_horizon=args.time_horizon,
            event_risk=args.event_risk,
        )
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"Risk: {result['risk']}")
    print(f"Reward: {result['reward']}")
    print(f"Risk/reward ratio: {result['risk_reward_ratio']}")
    print(f"Asymmetry: {result['asymmetry']}")
    print(f"Primary concern: {result['primary_concern']}")
    print(f"What must be true: {result['what_must_be_true']}")
    if result["structural_flags"]:
        print("Structural flags:")
        for flag in result["structural_flags"]:
            print(f"- {flag}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
