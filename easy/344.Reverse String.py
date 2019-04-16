"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.


Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""


def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    # 172 ms, faster than 68.76%.
    swap_length = len(s)//2
    for i in range(swap_length):
        temp = s[i]
        s[i] = s[-i-1]
        s[-i-1] = temp


def reverseString2(s: list[str]) -> None:
    # 164 ms, faster than 78.93%, the best solution from submissions (144 ms).
    s.reverse()