from __future__ import annotations

import math

from tests.helpers import import_module_from_path


def load_calculations(repo_root):
    return import_module_from_path(
        "trading_skill_calculations",
        repo_root / "skills" / "_lib" / "calculations.py",
    )


def test_fixed_fractional_position_size(repo_root):
    calculations = load_calculations(repo_root)
    result = calculations.fixed_fractional_position_size(
        account_equity=100_000,
        entry_price=100,
        stop_price=95,
        risk_fraction=0.01,
    )
    assert result["risk_budget"] == 1000
    assert result["unit_risk"] == 5
    assert result["size"] == 200
    assert result["total_risk"] == 1000


def test_volatility_adjusted_position_size(repo_root):
    calculations = load_calculations(repo_root)
    result = calculations.volatility_adjusted_position_size(
        account_equity=50_000,
        average_true_range=2.5,
        atr_multiple=1.5,
        risk_amount=500,
    )
    assert result["synthetic_stop_distance"] == 3.75
    assert math.isclose(result["raw_size"], 133.3333333333, rel_tol=1e-6)
    assert result["size"] == 133


def test_kelly_fraction(repo_root):
    calculations = load_calculations(repo_root)
    result = calculations.kelly_fraction(
        win_rate=0.55,
        average_win=1.5,
        average_loss=1.0,
        cap_fraction=0.2,
    )
    assert math.isclose(result["raw_fraction"], 0.25, rel_tol=1e-9)
    assert result["capped_fraction"] == 0.2


def test_risk_reward_and_expectancy(repo_root):
    calculations = load_calculations(repo_root)
    ratio = calculations.risk_reward_ratio(
        entry_price=100,
        stop_price=95,
        target_price=110,
    )
    expectancy = calculations.expectancy(
        win_rate=0.4,
        average_win=10,
        average_loss=5,
    )
    assert ratio["ratio"] == 2
    assert expectancy["expectancy"] == 1
    assert expectancy["expectancy_r"] == 0.2


def test_futures_contract_risk(repo_root):
    calculations = load_calculations(repo_root)
    result = calculations.futures_contract_risk(
        entry_price=5200,
        stop_price=5195,
        contract_multiplier=50,
        contracts=2,
        slippage_per_contract=12.5,
        fee_per_contract=2.5,
    )
    assert result["per_contract_risk"] == 265
    assert result["total_risk"] == 530


def test_trade_statistics(repo_root):
    calculations = load_calculations(repo_root)
    result = calculations.trade_statistics([2.0, -1.0, 1.5, -0.5, 0.0])
    assert result["trades"] == 5
    assert result["wins"] == 2
    assert result["losses"] == 2
    assert result["breakeven"] == 1
    assert math.isclose(result["win_rate"], 0.4, rel_tol=1e-9)
    assert math.isclose(result["profit_factor"], 7 / 3, rel_tol=1e-9)
