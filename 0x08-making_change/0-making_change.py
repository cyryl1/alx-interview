#!/usr/bin/python3
"""Minimum number of coin"""


def makeChange(coins, total):
    """makeChange function"""
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for x in range(1, total + 1):
        for c in coins:
            if x >= c:
                dp[x] = min(dp[x], dp[x - c] + 1)

    print(dp[total] if dp[total] != float('inf') else -1)
