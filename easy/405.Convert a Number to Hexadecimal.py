"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:
    All letters in hexadecimal (a-f) must be in lowercase.
    The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
    The given number is guaranteed to fit within the range of a 32-bit signed integer.
    You must not use any method provided by the library which converts/formats the number to hex directly.

Example 1:
    Input: 26
    Output: "1a"

Example 2:
    Input: -1
    Output:
    "ffffffff"
"""


def toHex(num: int) -> str:
    """
    :type num: int
    :rtype: str
    """
    # 36 ms, faster than 80.93%.
    res = ""
    dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
           8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: '0'}
    if num > 0:
        while num > 0:
            res = dic[num % 16] + res
            num //= 16
    elif num < 0:
        posi, extra = -num, 1  # *** the result of negative number divide positive number: -1//16 = -1.
        while posi > 0:
            res = dic[15 - posi % 16 + extra] + res
            if posi%16 != 0:
                extra = 0
            posi //= 16
        res = 'f' * (8 - len(res)) + res
    else:
        return '0'
    return res


def toHex2(num):
    if num == 0:
        return '0'
    hd = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    res = []
    c = 0
    while num and c < 8:
        res.insert(0, hd[num & 15])
        num >>= 4
        c += 1
    return ''.join(res)


def toHex3(num):
    # 36 ms, faster than 80.93%. The best solution from submissions (28 ms).
    ans = ""
    for _ in range(8):4
        num, r = divmod(num, 16)  # *** divmod() div, mod
        ans = "0123456789abcdef"[r] + ans
        if num == 0:
            break
    return ans


print(toHex(26)) # 1a
print(toHex(-1)) # ffffffff
print(toHex(100000)) # 186a0
print(toHex(-100000)) # fffe7960
print(-1/16)