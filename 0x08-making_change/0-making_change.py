#!/usr/bin/python3
"""
`0-making_change` module
"""


def makeChange(coins, total):
    """
    returns lowest number of coins needed to make
    total
    """
    coins.sort(reverse=True)
    numberCoins = 0
    totalCost = 0
    coinsUsed = []
    for coin in coins:
        while coin + totalCost <= total:
            totalCost += coin
            numberCoins += 1
            if totalCost == total:
                return numberCoins
    return -1
