"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
    Input: "Hello"
    Output: "hello"

Example 2:
    Input: "here"
    Output: "here"

Example 3:
    Input: "LOVELY"
    Output: "lovely"
"""

def toLowerCase(str: str) -> str:
    # 28 ms, faster than 98.62%
    res = ''
    diff = ord('a') - ord('A')
    for c in str:
        if c.isupper():
            res += chr(ord(c) + diff)
        else:
            res += c
    return res