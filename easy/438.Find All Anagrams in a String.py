from collections import Counter
"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:
    Input: s: "cbaebabacd" p: "abc"
    Output: [0, 6]
    Explanation:
        The substring with start index = 0 is "cba", which is an anagram of "abc".
        The substring with start index = 6 is "bac", which is an anagram of "abc".

    Example 2:
    Input: s: "abab" p: "ab"
    Output: [0, 1, 2]
    Explanation:
        The substring with start index = 0 is "ab", which is an anagram of "ab".
        The substring with start index = 1 is "ba", which is an anagram of "ab".
        The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


def findAnagrams(s: str, p: str):  # -> list[int]:
    """ # Time limit exceed.
    pl, sl, res = len(p), len(s), []
    if pl <= sl:
        count = [Counter(s[i:i + pl]) for i in range(sl - pl + 1)] + [Counter(p)]
        for i in range(len(count) - 1):
            if count[i] == count[-1]: res.append(i)
    return res
    """

def findAnagrams2(s: str, p: str):  # -> list[int]:
    # 116 ms, faster than 87.64
    def countarr(w):
        out = [0]*26
        for c in w:
            out[ord(c)-ord('a')]+=1
        return out

    m = len(p)
    ps = countarr(p)
    ans = []
    ss = countarr(s[:m])

    if ss == ps:
        ans = [0]

    for i in range(1,len(s)-m+1):

        left = ord(s[i-1])-ord('a')
        right = ord(s[i+m-1])-ord('a')
        ss[left] = ss[left] -1
        ss[right] = ss[right] +1

        if ss == ps:
            ans.append(i)
    return ans

def findAnagrams3(s: str, p: str):  # -> list[int]:
    # 92 ms, faster than 99.64%. The best solution from submissions (84 ms)
    len_p = len(p)
    if not s or len(s) < len_p:
        return []
    ans = []
    hs, hp = 0, 0
    for i in range(len_p):
        hs += hash(s[i])   # *** hash(): return the hash value of the object (if it has one). Hash values are integers.
        hp += hash(p[i])
    if hs == hp:
        ans.append(0)
    for right in range(len_p, len(s)):
        left = right - len_p
        hs += hash(s[right]) - hash(s[left])
        if hs == hp:
            ans.append(left + 1)
    return ans


print(findAnagrams3("abab", "ab"))
print(hash('a'))