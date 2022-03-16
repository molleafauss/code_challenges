import itertools
"""
  Given a list of integer, representing rates of a stock during a day, find the maximum profit that could have been made
  by buying low and selling hig during that day.
  
  (Toast - also failed during the hour of interview)   
"""
WINDOW = 5

def max_delta(values):
    if len(values) < WINDOW:
        return 0
    pos = 0
    state = {
        "min_pos": pos,
        "dmin": pos,
        "dmax": pos,
        "delta": 0
    }
    pos = WINDOW
    while pos < len(values):
        delta = values[pos] - values[state["min_pos"]]
        if delta > state["delta"]:
            state["dmax"] = pos
            state["dmin"] = state["min_pos"]
            state["delta"] = delta

        back = pos - WINDOW + 1
        if values[back] < values[state["min_pos"]]:
            state["min_pos"] = back

        pos += 1

    print("Result is %(delta)s, between items at %(dmin)s<->%(dmax)s" % state)

    return state["delta"]


def check(prices, expected):
    result = max_delta(prices)
    if result != expected:
        print("[FAIL] expected %d, found %d (input %s)" % (expected, result, prices))
    else:
        print("[ OK ] Found correct result %d for %s" % (expected, prices))


if __name__ == '__main__':
    check([3, 2, 5, 6, 3, 15, 7], 12)
    check([4, 2, 5, 6, 3, 15, 14], 12)
    check([7, 6, 5, 4, 3, 2, 1], 0)
    check([7, 6, 7, 6, 7, 6, 7], 1)
    check([7, 6, 7, 6, 7, 6], 0)
    check([7, 6, 5, 8, 10, 12, 11, 12, 8, 10, 13, 17, 11], 12)
    check([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6], 5)
    check([3, 2, 4, 6, 9, 5, 4, 2, 3, 5, 6, 5, 4, 6, 7, 6], 5)
    check([3, 2, 4, 6, 9, 5, 4, 2, 3, 5, 7, 5, 4, 6, 5, 6], 5)
    check([3, 2, 4, 6, 9, 5, 4, 2, 3, 5, 6], 4)
