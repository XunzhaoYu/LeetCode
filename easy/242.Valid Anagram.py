"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


def isAnagram(s: str, t: str) -> bool:  # 52 ms, faster than 81.38%.
    if set(s) != set(t):
        return False
    dic = {}
    for c in set(s):
        dic[c] = 0
    for c in s:
        dic[c] += 1
    for c in t:
        dic[c] -= 1
    for v in dic.values():
        if v != 0:
            return False
    return True


def isAnagram2(s: str, t: str) -> bool:  # 68 ms
    return sorted(s) == sorted(t)


def isAnagram2(s: str, t: str) -> bool:  # 40 ms, faster than 99.14%. The best solution from submissions (36 ms)
    return all(s.count(c) == t.count(c) for c in 'abcdefghijklmnopqrstuvwxyz')  # *** s.count()


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))


