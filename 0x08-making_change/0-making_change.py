#!/usr/bin/python3
"""Minimum number of coin"""

def makeChange(coins, total):
    """makeChange function"""
    if total <= 0:
        return 0
    n = len(coins)
    ans = []

    i = n - 1
    while(i >= 0):
        while (total >= coins[i]):
            total -= coins[i]
            ans.append(coins[i])
        i -= i
    for i in range(len(ans)):
        print(ans[i], end=" ")


print(makeChange([1, 2, 25], 37))
print(makeChange([1256, 54, 48, 16, 102], 1453))
