from string import ascii_lowercase as letters
import datetime as dt
from collections import defaultdict
from itertools import combinations
from vierkante_tafel_util import draw


def gen_people():
    gen_name = (x + y for x in letters for y in letters)
    return [next(gen_name) for _ in range(0, 50)]


def test_all():
    people = gen_people()
    hist = list()
    now = dt.date.today()
    dates = [
        (now - dt.timedelta(days=2 * 365)) + dt.timedelta(days=x * 14)
        for x in range(0, 104)
    ]
    for d in dates:
        group = draw(d, people, hist)
        hist.append({"group": group, "date": d})

    occ = defaultdict(int)

    for h in hist:
        d = h["date"]
        g = h["group"]
        # print(f"{d.isoformat()} - {g}")
        for p in g:
            occ[p] = occ[p] + 1
    cnts = occ.values()
    assert max(cnts) - min(cnts) <= 2

    u = list()
    for c in occ.keys():
        z = sorted([x["date"] for x in hist if c in x["group"]])
        k = [z[i + 1] - z[i] for i in range(0, len(z) - 1)]
        u.append(min(k))

    assert min(u).days > 15

    together = defaultdict(int)
    for h in hist:
        for p1, p2 in combinations(h["group"], 2):
            k = "_".join(sorted([p1, p2]))
            together[k] = together[k] + 1

    assert(max(together.values()) <= 4)
    # print(sorted(together.items(), key=lambda kv: kv[1], reverse=True))
