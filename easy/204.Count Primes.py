import numpy as np
"""
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""


def countPrimes(n):  # 1712 ms, faster than 16.39%.
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    res, sieve = [True] * n, 2
    while sieve ** 2 < n:
        for i in range(2, (n-1) / sieve+1):  # tested all integers as sieves, wasted too much time here.
            res[i * sieve] = False
        sieve += 1
    return sum(res)-2


def countPrimes2(n):  # 268 ms, faster than 84.76%
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:  # idea: tested only primes as sieves. ***
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  # *** array[start: end: interval]
    return sum(primes)  # *** sum trues.


def countPrimes3(n):  # 44 ms, faster than 100.00%.
    if n <= 2:
        return 0
    blacklist = np.ones(((n-2) // 2, ), dtype=np.bool)
    threshold = int(math.sqrt(n))+1
    for i in range(3, threshold, 2):  # *** idea: tested only primes as sieves, and ignored all even numbers.
        if blacklist[(i-3) // 2]:
            # Use the list comprehension to update
            blacklist[(i * i - 3) // 2: n: i] = False
    return int(np.sum(blacklist)) + 1


print(countPrimes(2))
print(countPrimes(10))
a = np.linspace(0, 1, 11)
print a
print a[1:10:3]