"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
    Input: 1
    Output: "1"

Example 2:
    Input: 4
    Output: "1211"
"""


import re


def countAndSay(n):  # 20ms, faster than 96.87%
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return '1'
    else:
        prev_str = countAndSay(n-1)
        count = 1
        curr_str = ""
        for i in range(len(prev_str)-1):
            if prev_str[i] != prev_str[i+1]:
                curr_str += str(count)
                curr_str += prev_str[i]
                count = 1
            else:
                count += 1
        curr_str += str(count)
        curr_str += prev_str[-1]
        return curr_str


def countAndSay2(n):  # 16 ms, faster than 100%.
    s = '1'
    for _ in range(n-1):  # ***
        let, temp, count = s[0], '', 0
        for l in s:
            if let == l:
                count += 1
            else:
                temp += str(count)+let
                let = l
                count = 1
        temp += str(count)+let  # ***
        s = temp
    return s


def countAndSay3(n):  # 36 ms, slow
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)  # *** lambda operation and regular expression, group(0) equivalent to group()
    return s


test_input = 1
print(countAndSay(test_input))  # 1
test_input = 2
print(countAndSay(test_input))  # 11
test_input = 3
print(countAndSay(test_input))  # 21
test_input = 4
print(countAndSay(test_input))  # 1211
test_input = 5
print(countAndSay(test_input))  # 111221
