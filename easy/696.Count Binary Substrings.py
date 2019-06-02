"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
    Input: "00110011"
    Output: 6
    Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
                Notice that some of these substrings repeat and are counted the number of times they occur.
                Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

    Example 2:
    Input: "10101"
    Output: 4
    Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

    Note:
        s.length will be between 1 and 50,000.
        s will only consist of "0" or "1" characters.
"""


def countBinarySubstrings(s):# str) -> int:
    # 172 ms, faster than 64.53%.
    res, count, cur = 0, [0, 0], int(s[0])
    count[cur] += 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count[cur] += 1
        else:
            res += min(count)
            cur = 1 - cur
            count[cur] = 1
    return res + min(count)


def countBinarySubstrings2(s):# str) -> int:
    # 96 ms, best solution from submissions.
    last = s[0]
    curLength = lastLength = res = 0
    for c in s:
        if c == last:
            curLength += 1
        else:
            last = c
            res += curLength if curLength < lastLength else lastLength
            lastLength = curLength
            curLength = 1
    res += curLength if curLength < lastLength else lastLength
    return res
