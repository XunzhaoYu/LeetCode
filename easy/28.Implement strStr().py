"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
    Input: haystack = "hello", needle = "ll"
    Output: 2

Example 2:
    Input: haystack = "aaaaa", needle = "bba"
    Output: -1

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if not needle:
        return 0
    length = len(needle)
    for i in range(len(haystack)-length+1):
        if haystack[i:i+length] == needle:
            return i
    return -1


test_input_argu1 = "hello"
test_input_argu2 = "ll"
print(strStr(test_input_argu1, test_input_argu2))

test_input2_argu1 = "aaaaa"
test_input2_argu2 = "bba"
print(strStr(test_input2_argu1, test_input2_argu2))
