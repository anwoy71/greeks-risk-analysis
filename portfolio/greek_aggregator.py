import pandas as pd
from pricing.black_scholes import delta, gamma, vega, theta

def compute_position_greeks(row):
    S = row["S"]
    K = row["K"]
    T = row["T"]
    r = row["r"]
    sigma = row["sigma"]
    option_type = row["option_type"]
    qty = row["quantity"]

    pd_ser = pd.Series({
        "delta": delta(S,K,T,r,sigma,option_type) * qty,
        "gamma": gamma(S,K,T,r,sigma) * qty,
        "vega":  vega(S,K,T,r,sigma) * qty,
        "theta": theta(S,K,T,r,sigma,option_type) * qty
    })
    return pd_ser


def aggregate_portfolio(df):
    greeks = df.apply(compute_position_greeks, axis=1)
    totals = greeks.sum()

    return totals