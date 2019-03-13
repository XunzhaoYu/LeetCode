"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
    Input: "()"
    Output: true

Example 2:
    Input: "()[]{}"
    Output: true

Example 3:
    Input: "(]"
    Output: false

Example 4:
    Input: "([)]"
    Output: false

Example 5:
    Input: "{[]}"
    Output: true
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    map = {"(": 1,
           ")": -1,
           "[": 2,
           "]": -2,
           "{": 3,
           "}": -3}
    stack = []
    valid = True
    for c in s:
        if map[c] > 0:
            stack.append(map[c])
        else:
            try:
                last_bracket = stack.pop(-1)
            except IndexError:
                return False
            if last_bracket + map[c] != 0:
                valid = False
                break
    if stack:
        valid = False
    return valid


def isValid2(s):
    map = {")": "(",  # ***
           "]": "[",
           "}": "{"}
    stack = []
    for c in s:
        if c in map:
            top_element = stack.pop() if stack else "#"  # ***
            if top_element != map[c]:
                return False
        else:
            stack.append(c)
    return not stack


test_input = "()"
print(isValid(test_input))
test_input2 = "()[]{}"
print(isValid(test_input2))
test_input3 = "(]"
print(isValid(test_input3))
test_input4 = "([)]"
print(isValid(test_input4))
test_input5 = "{[]}"
print(isValid(test_input5))
