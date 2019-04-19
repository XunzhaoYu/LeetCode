from collections import Counter
"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
    You may assume that both strings contain only lowercase letters.

Examples:
    canConstruct("a", "b") -> false
    canConstruct("aa", "ab") -> false
    canConstruct("aa", "aab") -> true
"""


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    # 108 ms, faster than 30.19%
    a, b = map(Counter, (ransomNote, magazine))
    return list((a-b).elements()) == []


def canConstruct2(ransomNote, magazine):
    # 28 ms, faster than 98.61%, the best solution form submissions (24 ms).
    return all([ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote)]) # *** review count().



print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
