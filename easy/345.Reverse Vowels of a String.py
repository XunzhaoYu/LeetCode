"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
    Input: "hello"
    Output: "holle"

Example 2:
    Input: "leetcode"
    Output: "leotcede"

Note:
    The vowels does not include the letter "y".
"""


def reverseVowels(s: str) -> str:
    # 56 ms, faster than 99.57%.
    vowels = "aeiouAEIOU"
    reverse_chars = [c for c in s if c in vowels]
    res, index = "", -1
    for c in s:
        if c in vowels:
            res += reverse_chars[index]
            index -= 1
        else:
            res += c
    return res


def reverseVowels2(s: str) -> str:
    # 56 ms, faster than 99.57%. Best solution from submissions (52 ms)
    vowels = set(list('aeiouAEIOU'))
    s = list(s)
    start = 0
    end = len(s) -1
    while start < end:
        if s[start] in vowels and s[end] in vowels:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        else:
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1
    return ''.join(s)  # *** review.