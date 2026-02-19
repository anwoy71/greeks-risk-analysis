import numpy as np
from scipy.stats import norm

# reference : sheldon natenberg - option volatility and pricing

# std dist between spot and strike price
def d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

def d2(S, K, T, r, sigma):
    return d1(S, K, T, r, sigma) - sigma * np.sqrt(T)


# option price
def option_price(S, K, T, r, sigma, option_type):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)

    if option_type == "call":
        return S * norm.cdf(D1) - K * np.exp(-r*T) * norm.cdf(D2)
    else:
        return K * np.exp(-r*T) * norm.cdf(-D2) - S * norm.cdf(-D1)

# greeks
def delta(S, K, T, r, sigma, option_type):
    D1 = d1(S, K, T, r, sigma)
    if option_type == "call":
        return norm.cdf(D1)
    else:
        return norm.cdf(D1) - 1

def gamma(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return norm.pdf(D1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    D1 = d1(S, K, T, r, sigma)
    return S * norm.pdf(D1) * np.sqrt(T)

def theta(S, K, T, r, sigma, option_type):
    D1 = d1(S, K, T, r, sigma)
    D2 = d2(S, K, T, r, sigma)

    first = -(S * norm.pdf(D1) * sigma) / (2 * np.sqrt(T))

    if option_type == "call":
        second = -r * K * np.exp(-r*T) * norm.cdf(D2)
        return first + second
    else:
        second = r * K * np.exp(-r*T) * norm.cdf(-D2)
        return first + second
