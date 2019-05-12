"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
    Input: "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""


def reverseWords(s: str) -> str:
    # 32 ms, faster than 99.77%. best is 28 ms.
    words = s.split()
    for i, w in enumerate(words):
        words[i] = w[::-1]
    return " ".join(words)