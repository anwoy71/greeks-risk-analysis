import pandas as pd
import statsmodels.api as sm


def run_regression(df):
    """
    df must contain:
    ['pnl', 'delta', 'gamma', 'vega', 'theta']
    """

    X = df[["delta", "gamma", "vega", "theta"]]
    y = df["pnl"]

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    return model
