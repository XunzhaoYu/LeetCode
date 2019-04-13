"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

Example 2:
    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false

Example 3:
    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

Example 4:
    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

Similar to problem 205. Isomorphic Strings.
"""


def wordPattern(pattern: str, str: str) -> bool:
    # 36 ms, faster than 76.09%, same to the best solution from submissions(28 ms)
    words, dictionary = str.split(), {}
    if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
        return False
    for i, c in enumerate(pattern):
        if c in dictionary and dictionary[c] != words[i]:
            return False
        else:
            dictionary[c] = words[i]
    return True



