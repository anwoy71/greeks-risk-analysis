def approximate_pnl(delta, gamma, vega, theta, dS=0, dVol=0, dT=0):
    """
    Greek-based PnL approx-
    dS   : change in underlying price
    dVol : change in volatility (absolute, e.g. 0.02 for +2%)
    dT   : change in time (in years, e.g. -1/365 for one day decay)
    """

    pnl = (delta*dS + 0.5*gamma*(dS**2) + vega*dVol + theta*dT)

    return pnl
