"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
    Input: "aba"
    Output: True

Example 2:
    Input: "abca"
    Output: True
    Explanation: You could delete the character 'c'.

Note:
    The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""


def validPalindrome(s: str) -> bool:
    # 88 ms, faster than 92.44%. Same as the best solution from submissions (60 ms)
    sp, ep = 0, len(s) - 1
    while sp < ep:
        if s[sp] != s[ep]:
            dis = (ep - sp) // 2
            return s[sp:sp + dis] == s[ep - 1:ep - dis - 1:-1] or s[sp + 1:sp + dis + 1] == s[ep:ep - dis:-1]
        else:
            sp += 1
            ep -= 1
    return True