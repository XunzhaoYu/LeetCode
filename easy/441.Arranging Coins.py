"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
    n = 5
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤
    Because the 3rd row is incomplete, we return 2.

Example 2:
    n = 8
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    Because the 4th row is incomplete, we return 3.
"""


def arrangeCoins(n: int) -> int:
    """ # 856 ms, faster than 45.115
    res = 0
    while n >= 0:
        res += 1
        n -= res
    return res-1
    """
    # 40 ms, faster than 100%.
    return int(math.sqrt(2 * n + 0.25) - 0.5)
    # (1+N)N/2 <= n < (2+N)N/2
    # N + N^2 <= 2n < 2N + N^2
    # (N + 0.5)^2 <= 2n + 0.25 < (N + 1)^2 - 0.75
    # N <= sqrt(2n + 0.25) - 0.5