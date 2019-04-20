"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""


def firstUniqChar(s: str) -> int:
    # 92 ms, faster than 87.19%.
    dic = {}
    for c in set(s):
        dic[c] = -1
    for i, c in enumerate(s):
        if c in dic:
            if dic[c] == -1:
                dic[c] = i
            else:
                dic.pop(c)
    if dic.values():
        return min(dic.values())
    else:
        return -1


def firstUniqChar2(s: str) -> int:
    # 88 ms, faster than 88.02%.
    dic = {}
    for c in set(s):
        dic[c] = s.count(c)
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


def firstUniqChar3(s: str) -> int:
    # 36 ms, faster than 100%. The best solution from submissions.
    alphabet, ans = string.ascii_lowercase, float('inf')  # ***
    for c in alphabet:
        i = s.find(c)  # *** 
        if i == -1:
            continue
        j = s.find(c, i + 1)
        if j == -1:
            ans = min(ans, i)
    return ans if ans != float('inf') else -1


print(firstUniqChar("leetcode"))
print(firstUniqChar("cc"))

