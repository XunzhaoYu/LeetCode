"""
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
    Input: 5
    Output: True
    Explanation: The binary representation of 5 is: 101

Example 2:
    Input: 7
    Output: False
    Explanation: The binary representation of 7 is: 111.

Example 3:
    Input: 11
    Output: False
    Explanation: The binary representation of 11 is: 1011.

Example 4:
    Input: 10
    Output: True
    Explanation: The binary representation of 10 is: 1010.
"""


def hasAlternatingBits(n):# int) -> bool:
    # 32 ms, faster than 94.21%.
    alt, extra = 1, 0
    while n > alt:
        alt = alt * 2 + extra
        extra = 1 - extra
    return n == alt

def hasAlternatingBits2(n):# int) -> bool:
    # 28 ms, faster than 99.25%
    pr = -1
    while n > 1:
        n, r = divmod(n, 2)
        if pr == r:
            return False
        else:
            pr = r
    return n != pr

def hasAlternatingBits3(n):# int) -> bool:
    # 28 ms, the best solution from submissions (20 ms)
    b = bin(n)
    for i in range(len(b) - 1):
        if b[i] == b[i + 1]:
            return False
    return True
