"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


def romanToInt(s):  # 80 ms less than 76.92%, 10.4 MB less than 100%
    """
    :type s: str
    :rtype: int
    """
    # 1000: M, 100: CDM, 10: XLC, 1: IVX
    nums = []
    for i in range(len(s)):
        if s[i] == "M":
            nums.append(1000)
        elif s[i] == "D":
            nums.append(500)
        elif s[i] == "C":
            nums.append(100)
        elif s[i] == "L":
            nums.append(50)
        elif s[i] == "X":
            nums.append(10)
        elif s[i] == "V":
            nums.append(5)
        elif s[i] == "I":
            nums.append(1)
    result = 0
    i = 0
    max_index = len(nums)-1
    while i < max_index:
        if nums[i] >= nums[i+1]:
            result += nums[i]
            i += 1
        else:
            result += nums[i+1]-nums[i]
            i += 2
    if i == max_index:
        result += nums[i]
    return result


def romanToInt2(s):  # 68 ms faster than 100%
    roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    prev, res = 0, 0
    for c in s:
        curr = roman[c]
        res += curr
        if curr > prev:
            res -= 2*prev
        prev = curr
    return res


test_input = "IX"  # 9
test_input2 = "LVIII"  # 58
test_input3 = "MCMXCIV"  # 1994
test_input4 = "DCXXI"  # 621
print(romanToInt2(test_input))
print(romanToInt2(test_input2))
print(romanToInt2(test_input3))
print(romanToInt2(test_input4))
