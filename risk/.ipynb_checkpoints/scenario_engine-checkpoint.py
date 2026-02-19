import pandas as pd
from risk.pnl_approximation import approximate_pnl


def run_scenarios(net_greeks, S,
                  price_shocks,
                  vol_shocks,
                  time_shock=0):
    """
    net_greeks : Series with delta, gamma, vega, theta
    S          : current underlying price
    price_shocks : list of % shocks (e.g. [-0.02, 0.02])
    vol_shocks   : list of absolute vol shocks (e.g. [-0.02, 0.02])
    time_shock   : time decay in years (default 0)
    """

    results = []

    for ps in price_shocks:
        for vs in vol_shocks:

            dS = S * ps
            dVol = vs

            pnl = approximate_pnl(
                net_greeks["delta"],
                net_greeks["gamma"],
                net_greeks["vega"],
                net_greeks["theta"],
                dS=dS,
                dVol=dVol,
                dT=time_shock
            )

            results.append({
                "price_shock_%": ps,
                "vol_shock": vs,
                "estimated_pnl": pnl
            })

    return pd.DataFrame(results)
