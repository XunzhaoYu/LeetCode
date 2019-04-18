"""
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
    Input: a = 1, b = 2
    Output: 3

Example 2:
    Input: a = -2, b = 3
    Output: 1
"""


def getSum(a: int, b: int) -> int:
    # Time Limit Exceeded.
    List = []
    if a >= 0 and b >= 0:
        for _ in range(a):
            List.append(1)
        for _ in range(b):
            List.append(1)
        return len(List)
    elif a < 0 and b < 0:
        for _ in range(-a):
            List.append(1)
        for _ in range(-b):
            List.append(1)
        return -len(List)
    elif abs(a) >= abs(b):
        for _ in range(abs(a)):
            List.append(1)
        for _ in range(abs(b)):
            List.pop()
        return len(List) if a > 0 else -len(List)
    else:
        for _ in range(abs(b)):
            List.append(1)
        for _ in range(abs(a)):
            List.pop()
        return len(List) if b > 0 else -len(List)


def getSum2(a: int, b: int) -> int:
    # 36 ms, faster than 74.50%. The best solution from submissions (28 ms).
    end = 0x7FFFFFFF
    start = 0x80000000
    mask = 0xFFFFFFFF
    # a carry
    # b position
    while b != 0:
        # ^ get different bits and & gets double 1s, << moves carry
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask  # *** idea: using ^ to count diff bits, using & to count double 1 bits.
    # if a is negative, get a's 32 bits complement positive first
    # then get 32-bit positive's Python complement negative
    return a if a <= end else ~(a ^ mask)