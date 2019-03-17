"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
    Input: "Hello World"
    Output: 5
"""


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    res = 0
    if s:
        find_word = -1
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                find_word = i
                break
        for i in range(find_word, -1, -1):
            if s[i] != " ":
                res += 1
            else:
                break
    return res


def lengthOfLastWord2(s):
    if not s:
        return 0
    word_list = [word for word in s.split()]  # *** split
    if word_list:
        return len(word_list[-1])
    else:
        return 0


test_input = "Hello World"
print(lengthOfLastWord(test_input))
