"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
    Input: s = "egg", t = "add"
    Output: true

Example 2:
    Input: s = "foo", t = "bar"
    Output: false

Example 3:
    Input: s = "paper", t = "title"
    Output: true

Note:
    You may assume both s and t have the same length.
"""


def isIsomorphic(s, t):  # 28ms, faster than 89.57%.
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    mapping, length = {}, len(s)
    for i in range(length):
        if s[i] not in mapping:
            if t[i] not in mapping.values():  # ***
                mapping[s[i]] = t[i]
            else:
                return False
        elif mapping[s[i]] != t[i]:
            return False
    return True


def isIsomorphic2(s, t):  # 28ms, faster than 89.57%. Best solution from the submissions.
    if len(set(s))!=len(set(t)):
        return False
    s_dic={}
    for counter,i in enumerate(s):
        print(counter, i, s[counter], t[counter])
        if i not in s_dic:
            s_dic[i]=t[counter]
        else:
            if s_dic[i]!=t[counter]:
                return False
    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("ab", "aa"))
