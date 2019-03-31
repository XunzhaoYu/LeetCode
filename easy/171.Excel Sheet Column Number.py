"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
    Input: "A"
    Output: 1

Example 2:
    Input: "AB"
    Output: 28

Example 3:
    Input: "ZY"
    Output: 701
"""


def titleToNumber(s):  # 28 ms, faster than 81.12%. The best solution from submissions is same to my solution.
    """
    :type s: str
    :rtype: int
    """
    res = 0
    for char in s:
        res *= 26
        digit = ord(char) - 64
        res += digit
    return res


def titleToNumber2(s):  # not the fastest one, but it is shortest
    return reduce(lambda x,y:x*26+y,map(lambda x:ord(x)-ord('A')+1,s))  # *** map, reduce


test_input = "A"
print(titleToNumber(test_input))  # 1
test_input = "AB"
print(titleToNumber(test_input))  # 28
test_input = "ZY"
print(titleToNumber(test_input))  # 701

