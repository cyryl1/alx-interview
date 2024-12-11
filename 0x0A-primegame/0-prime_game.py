#!/usr/bin/python3
"""0-prime_game"""


def SieveOfEratosthenes(n):
    """
    An algorithm to filter out prime numbers
    in a range of numbers.

    Parameters
    n (int): The upper limit of the range.
    """
    prime = [True for i in range(n+1)]
    p = 2
    count = 0

    while (p * p <= n):
        if (prime[p] is True):
            # Check for multiples
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    for p in range(2, n+1):
        if prime[p]:
            # print(p)
            count += 1
    return count


def isWinner(x, nums):
    """
    Determine the winner of the game.
    Parameters:
    - x(num): The number of turns
    nums [list]: The range of each round
    """
    p1 = 0
    p2 = 0
    for i in range(x):
        n = nums[i]
        res = SieveOfEratosthenes(n)
        if res % 2 == 0:
            p2 += 1
        else:
            p1 += 1
    if p1 > p2:
        return "Maria"
    return "Ben"
