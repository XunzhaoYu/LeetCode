"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:
    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
"""


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits.insert(0, 0)
    for i in range(len(digits)-1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            break
        else:
            digits[i] = 0
    if digits[0] == 0:
        return digits[1:]
    else:
        return digits


def plusOne2(digits):
    n = len(digits)
    i = 0

    while i < n:
        temp = digits[n - 1 - i] + 1
        if temp <= 9:
            digits[n - 1 - i] = temp
            break
        else:
            digits[n - 1 - i] = 0
        i = i + 1

    if digits[0] == 0:  # *** logic
        digits.insert(0, 1)
    return digits


test_input = [1, 2, 3]
print(plusOne(test_input))
test_input = [4, 3, 2, 1]
print(plusOne(test_input))
test_input = [9]
print(plusOne(test_input))
test_input = [9, 9]
print(plusOne(test_input))
