"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring( s: str) -> int:
        # 808 ms, faster than 8.81%.
        sl = len(s)
        substrings = [i for i in range(sl)]
        res = 0
        while substrings:
            res += 1
            len_limit = sl - res
            temp = []
            for i, ss in enumerate(substrings):
                if ss < len_limit and s[ss+res] not in s[ss:ss+res]:
                    temp.append(ss)
            substrings = temp
        return res


def lengthOfLongestSubstring2( s: str) -> int:  # *** idea
        # 36 ms, best solution from submissions.
        ls = ''
        l = 0
        for c in s:
            if c in ls:
                if len(ls) > l:
                    l = len(ls)
                ls = ls[ls.index(c)+1:]
            ls+=c
        if len(ls) > l:
            l = len(ls)
        return l