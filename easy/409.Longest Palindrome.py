from collections import Counter
"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
    Assume the length of given string will not exceed 1,010.

Example:
    Input: "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


def longestPalindrome(s: str) -> int:
    # 36 ms, faster than 99.42%.
    res = len(s)
    for c in set(s):
        if s.count(c) % 2 == 1:
            res -= 1
    return min(res+1, len(s))


def longestPalindrome2(s: str) -> int:
    # 40 ms, faster than 76.67%. The best solution from submissions (32 ms).
    ctr = Counter(s)
    ans = 0
    flag = 0
    for a, c in ctr.items():
        if c & 1 == 0:
            ans += c
        else:
            ans += c - 1
            flag = 1
    return ans + 1 if flag else ans