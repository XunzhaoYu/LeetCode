"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 5
    Output: false

Follow up: Could you solve it without loops/recursion?
"""


def isPowerOfFour(num: int) -> bool:
    # implemented without a loop or a while. 36 ms, faster than 100.00%
    return num>0 and num & (num-1) == 0 and len(bin(num))%2 == 1



print(isPowerOfFour(16))
print(isPowerOfFour(5))
print(isPowerOfFour(8))
print(isPowerOfFour(-16))
