"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...

Example 1:
    Input: 1
    Output: "A"

Example 2:
    Input: 28
    Output: "AB"

Example 3:
    Input: 701
    Output: "ZY"
"""


def convertToTitle(n):  # 20 ms, faster than 51.08%
    """
    :type n: int
    :rtype: str
    """
    digit = (n-1) % 26
    res = chr(ord('A') + digit)
    n = (n - digit) / 26
    while n != 0:
        digit = (n-1) % 26
        res += chr(ord('A') + digit)   # *** chr(), ord()
        n = (n - digit) / 26
    return res[::-1]


def convertToTitle2(n):  # best solution (16 ms) from submissions, but tested to be 20 ms.
    res, n = '', n-1
    while n >= 0:
        res += chr(65 + n % 26)
        n = n/26 - 1
    return res[::-1]


test_input = 1
print(convertToTitle(test_input))  # A
test_input = 28
print(convertToTitle(test_input))  # AB
test_input = 701
print(convertToTitle(test_input))  # ZY

