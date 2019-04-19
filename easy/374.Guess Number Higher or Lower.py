"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
    Input: n = 10, pick = 6
    Output: 6
"""


def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    # 20 ms, faster than 67.60%. Same to the best solution from submissions(16 ms).
    start, end = 1, n + 1
    while start < end:
        mid = (start + end) // 2
        res = guess(mid)
        if res > 0:
            start = mid + 1
        elif res < 0:
            end = mid
        else:
            return mid