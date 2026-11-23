"""Shared functions for the disposable income model."""
import pandas as pd

CLEAN = "../data/clean/"
CITIES = ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"]
AWARD = {"Hospitality": "Restaurant Industry Award",
         "Retail": "General Retail Industry Award"}
HOUSING = {"Share room": "Share room", "Living alone": "All units"}
BASE_HOURS = {"Weekday": 12, "Saturday": 6, "Sunday": 6}   # 24 hours per week
MIX = {"Weekday": 0.5, "Saturday": 0.25, "Sunday": 0.25}   # share of hours by day type
LEVEL = "Level 1"
WEEKS = 52


def load_tables(path=CLEAN):
    names = ["fair_work_rates", "rent", "tax_rates", "lito", "insurance",
             "transport", "food_scenarios", "living_costs_other"]
    return {n: pd.read_csv(path + n + ".csv", keep_default_na=False, na_values=[""])
            for n in names}


def scale_hours(total):
    """Split a weekly total into weekday/Saturday/Sunday using the base mix."""
    return {d: total * share for d, share in MIX.items()}


def income_tax(income, residency, tables):
    t = tables["tax_rates"]
    t = t[t["residency"] == residency].copy()
    t["threshold"] = (t["income_from"] - 1).clip(lower=0)
    row = t[t["threshold"] < income].iloc[-1]
    return row["base_tax"] + row["rate"] * (income - row["threshold"])


def lito(income, tables):
    t = tables["lito"].copy()
    t["threshold"] = t["income_from"] - 1
    row = t[t["threshold"] < income].iloc[-1]
    return max(row["max_offset"] - row["reduction_rate"] * (income - row["reduction_starts_at"]), 0)


def net_income(income, residency, tables):
    tax = income_tax(income, residency, tables)
    if residency == "Resident":
        tax = max(tax - lito(income, tables), 0)
    return income - tax


def disposable_income(tables, city, industry="Hospitality", housing="Share room",
                      residency="Resident", hours=None, rent_shock=0.0,
                      transport=None, food=None):
    """Weekly disposable income for one scenario. Optional overrides for hours, rent, transport and food."""
    hours = hours or BASE_HOURS
    fw, rent = tables["fair_work_rates"], tables["rent"]

    gross = 0.0
    for day_type, h in hours.items():
        m = ((fw["award"] == AWARD[industry]) & (fw["level"] == LEVEL)
             & (fw["day_type"] == day_type))
        gross += fw.loc[m, "casual_hourly_rate"].iloc[0] * h
    net = net_income(gross * WEEKS, residency, tables) / WEEKS

    m = (rent["city"] == city) & (rent["housing_type"] == HOUSING[housing])
    rent_week = rent.loc[m, "weekly_rent"].iloc[0] * (1 + rent_shock)

    if transport is None:
        t = tables["transport"]
        transport = t[(t["city"] == city) & (t["scenario"] == "base")]["weekly_cost_aud"].iloc[0]
    if food is None:
        f = tables["food_scenarios"]
        food = f[(f["city"] == city) & (f["scenario"] == "base")]["food_weekly_aud"].iloc[0]

    oshc = tables["insurance"]["weekly_aud"].mean()
    other = tables["living_costs_other"].query("scenario == 'base'")["weekly_aud"].sum()
    essentials = rent_week + transport + oshc + food + other
    return {"gross": gross, "net": net, "rent": rent_week, "transport": transport,
            "oshc": oshc, "food": food, "other": other,
            "essentials": essentials, "disposable": net - essentials}