import math
import datetime as dt
from random import shuffle


def calc_weight(ndraws, ndays):
    if ndraws == 0 or ndays is None:
        return 1
    # every half year with sd of 60 days
    # or plot some random graphs and take the most beautiful one
    # this would correspond to P(X < ndays), I think
    # from scipy.stats import norm
    # p = norm.cdf(ndays, loc=180, scale=60)
    # but my simple approximation is much faster
    p = 1 / (1 + math.exp(-(ndays - 180) * 0.03))
    # you get punished if you have been selected multiple times
    u = 1 / (ndraws + 1)
    return p * u


def elapsed_days(draw, now):
    return (now - draw["date"]).days


def my_draws(c, draws):
    return [draw for draw in draws if c in draw["group"]]


def draws_sorted(draws):
    # oldest first
    return sorted(draws, key=lambda u: u["date"])


def draws_since(date, draws):
    return [draw for draw in draws if draw["date"] > date]


def draw(now, people, hist, group_size=4):
    shuffle(people)
    recent_hist = draws_sorted(draws_since(now - dt.timedelta(days=365), hist))

    blacklist = recent_hist[-1]["group"] if hist else []

    group = list()

    for _ in range(0, group_size):
        eligible = [p for p in people if p not in group and p not in blacklist]
        weights = [
            (p, calc_candidate_weight(p, group, now, recent_hist)) for p in eligible
        ]
        chosen = max(weights, key=lambda x: x[1])[0]
        group.append(chosen)

    return sorted(group)


def calc_candidate_weight(c, group, now, hist):
    prev_draws = draws_sorted(my_draws(c, hist))
    ndays = elapsed_days(prev_draws[-1], now) if prev_draws else None
    ndraws = len(prev_draws)

    # products are not numerically stable: they tend to converge quickly to zero or to infinity
    # therefore math.log (but the order stays the same)
    # related: https://stackoverflow.com/questions/2343093/what-is-log-likelihood
    weight = math.log(calc_weight(ndraws, ndays))

    for member in group:
        if member == c:
            continue
        prev_draws_shared = my_draws(member, prev_draws)
        ndays_shared = (
            elapsed_days(prev_draws_shared[-1], now) if prev_draws_shared else None
        )
        ndraws_shared = len(prev_draws_shared)

        weight = weight + math.log(calc_weight(ndraws_shared, ndays_shared))

    return weight
