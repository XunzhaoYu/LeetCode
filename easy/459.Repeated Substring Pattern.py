"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
    Input: "abab"
    Output: True
    Explanation: It's the substring "ab" twice.

Example 2:
    Input: "aba"
    Output: False

Example 3:
    Input: "abcabcabcabc"
    Output: True
    Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


def repeatedSubstringPattern(s: str) -> bool:
    res, sl = False, len(s)
    split = 2 if sl % 2 == 0 else 3
    f_end = sl // split + 1
    f_start = s.find(s[0], 1, f_end)
    while f_start > 0:
        sp = f_start + 1
        while sp < sl:
            if s[sp] != s[sp - f_start]:
                break
            else:
                sp += 1
        if sp == sl:
            return True
        f_start = s.find(s[0], f_start + 1, f_end)
    return False


print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
