"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
    n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
    Input: 3
    Output: 3

Example 2:
    Input: 11
    Output: 0
    Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""


def findNthDigit(n: int) -> int:
    # 36 ms, faster than 80.18%.
    if n < 10:
        return n
    digit_num, nn = 1, n - 9
    while nn > 0:
        n = nn
        digit_num += 1
        nn -= digit_num * 9 * 10 ** (digit_num - 1)
    num = (n - 1) // digit_num + 10 ** (digit_num - 1)
    digit = digit_num - (n - 1) % digit_num - 1
    print(num, digit)
    for _ in range(digit):
        num //= 10
    return num % 10


def findNthDigit(n: int) -> int:
    # 36 ms, faster than 80.18%. Best solution from submissions (28 ms).
    n -= 1
    for digit in range(1, 11):
        first = 10 ** (digit - 1)
        if n < 9 * digit * first:
            return int(str(first + n // digit)[n % digit])
        n -= 9 * digit * first
