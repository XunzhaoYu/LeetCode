"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Follow up:
Coud you solve it without converting the integer to a string?
"""


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] != x[j]:
            return False
        i += 1
        j -= 1
    return True


def isPalindrome2(x):  # 100%, but string
    """
    :type x: int
    :rtype: bool
    """
    x = str(x)
    y = x[::-1]
    return x == y


test_input = 121
print(isPalindrome2(test_input))
