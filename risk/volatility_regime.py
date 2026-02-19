import pandas as pd
import numpy as np


def compute_realized_vol(df, window=21):
    """
    df must contain column 'returns'
    window = rolling window (default 21 trading days ≈ 1 month)
    """

    df = df.copy()

    df["realized_vol"] = (
        df["returns"]
        .rolling(window)
        .std() * np.sqrt(252)
    )

    return df


def classify_regime(df, low_q=0.33, high_q=0.66):
    """
    Classify volatility regime based on quantiles
    """

    df = df.copy()

    low_thresh = df["realized_vol"].quantile(low_q)
    high_thresh = df["realized_vol"].quantile(high_q)

    def label(vol):
        if vol <= low_thresh:
            return "Low Vol"
        elif vol >= high_thresh:
            return "High Vol"
        else:
            return "Medium Vol"

    df["vol_regime"] = df["realized_vol"].apply(label)

    return df
