"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
"""


def addBinary2(a, b):  # 24 ms, faster than 86.51%
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if not a or not b:
        return a or b
    sum = str(int(a) + int(b))
    temp, res = 0, ""
    for i in range(len(sum) - 1, -1, -1):
        temp += int(sum[i])
        if temp >= 2:
            res += str(temp-2)
            temp = 1
        else:
            res += str(temp)
            temp = 0
    if temp == 1:
        res += "1"
    return res[::-1]


def addBinary(a, b):  # 20 ms or 16 ms, faster than 99.84% or 100%.
    if not a or not b:
        return a or b
    int_num = int(a, 2) + int(b, 2)
    bin_num = bin(int_num)[2:]  # *** built-in function "bin()"
    return bin_num


test_input_a, test_input_b = "11", "1"
print(addBinary(test_input_a, test_input_b))  # "100"
test_input_a, test_input_b = "1010", "1011"
print(addBinary(test_input_a, test_input_b))  # "10101"
test_input_a, test_input_b = "1010", ""
print(addBinary(test_input_a, test_input_b))
test_input_a, test_input_b = "", "1011"
print(addBinary(test_input_a, test_input_b))