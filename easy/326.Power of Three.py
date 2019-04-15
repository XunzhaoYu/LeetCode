from math import math
"""
Given an integer, write a function to determine if it is a power of three.

Example 1:
    Input: 27
    Output: true

Example 2:
    Input: 0
    Output: false

Example 3:
    Input: 9
    Output: true

Example 4:
    Input: 45
    Output: false

Follow up:
    Could you do it without using any loop / recursion?
"""


def isPowerOfThree(n: int) -> bool:
    # implemented without a loop or a while. 128 ms, faster than 86.38%
    if n < 1:
        return False
    power = round(math.log(n) / math.log(3), 10)
    return power == power // 1
    """ # common method with a loop. 104 ms, best solution. 
    while n%3==0 and n!=0:
        n=n/3
    return n==1
    """