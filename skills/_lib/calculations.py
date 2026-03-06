"""Reusable quantitative helpers for trading-skills.

These functions are intentionally small, explicit, and dependency-free so
agents with code execution can use them without pulling in a larger framework.
All loss inputs should be passed as positive magnitudes rather than signed
negative values unless a function explicitly says otherwise.
"""

from __future__ import annotations

import math
from collections.abc import Sequence


def _resolve_risk_budget(
    *,
    account_equity: float,
    risk_fraction: float | None,
    risk_amount: float | None,
) -> float:
    if risk_amount is not None:
        if risk_amount <= 0:
            raise ValueError("risk_amount must be positive.")
        return float(risk_amount)
    if risk_fraction is None:
        raise ValueError("Provide either risk_fraction or risk_amount.")
    if not 0 < risk_fraction <= 1:
        raise ValueError("risk_fraction must be between 0 and 1.")
    if account_equity <= 0:
        raise ValueError("account_equity must be positive.")
    return float(account_equity) * float(risk_fraction)


def _round_down(value: float, increment: float) -> float:
    if increment <= 0:
        raise ValueError("rounding increment must be positive.")
    return math.floor(value / increment) * increment


def price_risk_per_unit(
    *,
    entry_price: float,
    stop_price: float,
    slippage_per_unit: float = 0.0,
    fee_per_unit: float = 0.0,
    contract_multiplier: float = 1.0,
) -> float:
    """Return all-in risk per unit or per contract."""
    if contract_multiplier <= 0:
        raise ValueError("contract_multiplier must be positive.")
    if entry_price <= 0 or stop_price <= 0:
        raise ValueError("entry_price and stop_price must be positive.")
    if slippage_per_unit < 0 or fee_per_unit < 0:
        raise ValueError("slippage_per_unit and fee_per_unit must be non-negative.")

    price_distance = abs(entry_price - stop_price)
    total_per_unit = price_distance + slippage_per_unit + fee_per_unit
    if total_per_unit <= 0:
        raise ValueError("Per-unit risk must be positive.")
    return total_per_unit * contract_multiplier


def fixed_fractional_position_size(
    *,
    account_equity: float,
    entry_price: float,
    stop_price: float,
    risk_fraction: float | None = None,
    risk_amount: float | None = None,
    slippage_per_unit: float = 0.0,
    fee_per_unit: float = 0.0,
    contract_multiplier: float = 1.0,
    round_lot: float = 1.0,
) -> dict[str, float]:
    """Size a position from a fixed risk budget."""
    risk_budget = _resolve_risk_budget(
        account_equity=account_equity,
        risk_fraction=risk_fraction,
        risk_amount=risk_amount,
    )
    unit_risk = price_risk_per_unit(
        entry_price=entry_price,
        stop_price=stop_price,
        slippage_per_unit=slippage_per_unit,
        fee_per_unit=fee_per_unit,
        contract_multiplier=contract_multiplier,
    )
    raw_size = risk_budget / unit_risk
    size = _round_down(raw_size, round_lot)
    total_risk = size * unit_risk
    return {
        "risk_budget": risk_budget,
        "unit_risk": unit_risk,
        "raw_size": raw_size,
        "size": size,
        "total_risk": total_risk,
    }


def volatility_adjusted_position_size(
    *,
    account_equity: float,
    average_true_range: float,
    atr_multiple: float = 1.0,
    risk_fraction: float | None = None,
    risk_amount: float | None = None,
    slippage_per_unit: float = 0.0,
    fee_per_unit: float = 0.0,
    contract_multiplier: float = 1.0,
    round_lot: float = 1.0,
) -> dict[str, float]:
    """Size a position from ATR-based stop distance."""
    if average_true_range <= 0:
        raise ValueError("average_true_range must be positive.")
    if atr_multiple <= 0:
        raise ValueError("atr_multiple must be positive.")

    synthetic_stop_distance = average_true_range * atr_multiple
    risk_budget = _resolve_risk_budget(
        account_equity=account_equity,
        risk_fraction=risk_fraction,
        risk_amount=risk_amount,
    )
    unit_risk = (synthetic_stop_distance + slippage_per_unit + fee_per_unit) * contract_multiplier
    raw_size = risk_budget / unit_risk
    size = _round_down(raw_size, round_lot)
    total_risk = size * unit_risk
    return {
        "risk_budget": risk_budget,
        "synthetic_stop_distance": synthetic_stop_distance,
        "unit_risk": unit_risk,
        "raw_size": raw_size,
        "size": size,
        "total_risk": total_risk,
    }


def kelly_fraction(
    *,
    win_rate: float,
    average_win: float,
    average_loss: float,
    cap_fraction: float | None = None,
) -> dict[str, float]:
    """Return raw and optionally capped Kelly fraction."""
    if not 0 <= win_rate <= 1:
        raise ValueError("win_rate must be between 0 and 1.")
    if average_win <= 0 or average_loss <= 0:
        raise ValueError("average_win and average_loss must be positive.")
    payoff_ratio = average_win / average_loss
    raw_fraction = win_rate - ((1 - win_rate) / payoff_ratio)
    capped_fraction = raw_fraction
    if cap_fraction is not None:
        if cap_fraction <= 0:
            raise ValueError("cap_fraction must be positive.")
        capped_fraction = max(min(raw_fraction, cap_fraction), -cap_fraction)
    return {
        "win_rate": win_rate,
        "payoff_ratio": payoff_ratio,
        "raw_fraction": raw_fraction,
        "capped_fraction": capped_fraction,
    }


def risk_reward_ratio(
    *,
    entry_price: float,
    stop_price: float,
    target_price: float,
    contract_multiplier: float = 1.0,
) -> dict[str, float]:
    """Return reward, risk, and reward-to-risk ratio."""
    if contract_multiplier <= 0:
        raise ValueError("contract_multiplier must be positive.")
    risk = abs(entry_price - stop_price) * contract_multiplier
    reward = abs(target_price - entry_price) * contract_multiplier
    if risk <= 0:
        raise ValueError("Risk must be positive.")
    return {
        "risk": risk,
        "reward": reward,
        "ratio": reward / risk,
    }


def expectancy(
    *,
    win_rate: float,
    average_win: float,
    average_loss: float,
) -> dict[str, float]:
    """Return expectancy in native units and loss-normalized R units."""
    if not 0 <= win_rate <= 1:
        raise ValueError("win_rate must be between 0 and 1.")
    if average_win < 0 or average_loss <= 0:
        raise ValueError("average_win must be non-negative and average_loss must be positive.")
    loss_rate = 1 - win_rate
    expectancy_value = (win_rate * average_win) - (loss_rate * average_loss)
    return {
        "win_rate": win_rate,
        "loss_rate": loss_rate,
        "expectancy": expectancy_value,
        "expectancy_r": expectancy_value / average_loss,
    }


def futures_contract_risk(
    *,
    entry_price: float,
    stop_price: float,
    contract_multiplier: float,
    contracts: float = 1.0,
    slippage_per_contract: float = 0.0,
    fee_per_contract: float = 0.0,
) -> dict[str, float]:
    """Return per-contract and total risk for futures-style instruments."""
    if contracts <= 0:
        raise ValueError("contracts must be positive.")
    per_contract_risk = price_risk_per_unit(
        entry_price=entry_price,
        stop_price=stop_price,
        slippage_per_unit=0.0,
        fee_per_unit=0.0,
        contract_multiplier=contract_multiplier,
    )
    friction = slippage_per_contract + fee_per_contract
    if friction < 0:
        raise ValueError("Contract friction inputs must be non-negative.")
    per_contract_all_in = per_contract_risk + friction
    return {
        "per_contract_risk": per_contract_all_in,
        "contracts": contracts,
        "total_risk": per_contract_all_in * contracts,
    }


def trade_statistics(results: Sequence[float]) -> dict[str, float]:
    """Summarize a sequence of trade results or R-multiples."""
    if not results:
        raise ValueError("results must not be empty.")

    wins = [value for value in results if value > 0]
    losses = [value for value in results if value < 0]
    breakeven = [value for value in results if value == 0]

    gross_profit = sum(wins)
    gross_loss = abs(sum(losses))
    average_win = gross_profit / len(wins) if wins else 0.0
    average_loss = gross_loss / len(losses) if losses else 0.0
    win_rate = len(wins) / len(results)
    expectancy_value = sum(results) / len(results)
    profit_factor = math.inf if gross_loss == 0 and gross_profit > 0 else (
        gross_profit / gross_loss if gross_loss > 0 else 0.0
    )

    running_pnl = 0.0
    running_peak = 0.0
    max_drawdown = 0.0
    for result in results:
        running_pnl += result
        running_peak = max(running_peak, running_pnl)
        max_drawdown = min(max_drawdown, running_pnl - running_peak)

    return {
        "trades": float(len(results)),
        "wins": float(len(wins)),
        "losses": float(len(losses)),
        "breakeven": float(len(breakeven)),
        "win_rate": win_rate,
        "average_win": average_win,
        "average_loss": average_loss,
        "gross_profit": gross_profit,
        "gross_loss": gross_loss,
        "net_result": sum(results),
        "expectancy": expectancy_value,
        "profit_factor": profit_factor,
        "max_drawdown": abs(max_drawdown),
    }
