#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    make change mthd
    """
    if total < 1:
        return 0
    coins.sort(reverse=True)
    x = 0
    for coin in coins:
        if total == 0:
            break
        num = total // coin
        total -= num * coin
        x += num
    return x if total == 0 else -1
