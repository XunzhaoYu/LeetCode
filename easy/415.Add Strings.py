from itertools import zip_longest
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def addStrings(num1: str, num2: str) -> str:
    # 44 ms, faster than 90.73%. The fastest solution used int(), which is not allowed here.
    longer, shorter = num1[::-1], num2[::-1]
    if len(longer) < len(shorter):
        longer, shorter = shorter, longer
    res, add, zero, nine = "", 0, ord('0'), ord('0') + 9
    for i in range(len(shorter)):
        temp = ord(longer[i]) + ord(shorter[i]) + add - zero
        if temp > nine:
            add, res = 1, chr(temp - 10) + res
        else:
            add, res = 0, chr(temp) + res
    for i in range(len(shorter), len(longer)):
        if add == 0:
            res = longer[i] + res
        elif longer[i] == '9':
            add, res = 1, '0'+res
        else:
            add, res = 0, chr(ord(longer[i])+1)+res
    return res if add == 0 else '1'+res


def addStrings2(num1: str, num2: str) -> str:
    # 48 ms, faster than 85.43%. Shortest solution from submissions.
    z = zip_longest(num1[::-1], num2[::-1], fillvalue='0')  # *** longest
    res, carry, zero2 = [], 0, 2 * ord('0')
    for i in z:
        cur_sum = ord(i[0]) + ord(i[1]) - zero2 + carry
        res.append(str(cur_sum % 10))
        carry = cur_sum // 10
    return ('1' if carry else '') + ''.join(res[::-1])


print(addStrings2("1", "9"))

