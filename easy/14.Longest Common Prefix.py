"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:
    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


def longestCommonPrefix(strs):  # 20 ms less than 96.43%, 10.8 MB less than 84.84%
    """
    :type strs: List[str]
    :rtype: str
    """
    length = 0
    stop = False
    num_strs = len(strs)
    if num_strs < 1:
        return ""
    elif num_strs == 1:
        return strs[0]
    max_length = len(strs[0])
    for i in range(1, num_strs):
        if max_length > len(strs[i]):
            max_length = len(strs[i])
    for i in range(max_length):
        for j in range(1, num_strs):
            if strs[j-1][i] != strs[j][i]:
                stop = True
                break
        if stop:
            break
        else:
            length += 1
    return strs[0][:length]


#  LCP(s1, s2, s3, s4) = LCP(LCP(LCP(s1, s2), s3), s4)
def longestCommonPrefix2(strs):  # 20 ms less than 96.29%, 10.7 MB less than 97.74%
    if not strs:  # ***
        return ""
    res = strs[0]
    prefix_len = len(res)
    del strs[0]   # ***
    for word in strs:
        prefix_len = min(prefix_len, len(word))  # ***
        for i in range(prefix_len):
            if res[i] != word[i]:
                prefix_len = i
                break
        if prefix_len == 0:
            break
    return res[:prefix_len]


test_input = ["flower", "flow", "flight"]
print(longestCommonPrefix2(test_input))
test_input2 = ["dog", "racecar", "car"]
print(longestCommonPrefix2(test_input2))
test_input3 = ["aa", "a"]
print(longestCommonPrefix2(test_input3))
test_input4 = ["a"]
print(longestCommonPrefix2(test_input4))
