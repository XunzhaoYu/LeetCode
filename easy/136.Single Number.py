"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""
from functools import reduce

def singleNumber(nums):  # system error, test running time in the future.
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for num in nums:
        res ^= num
    return res


def singleNumber2(nums):
    return reduce(operator.xor, nums)  # *** reduce:
# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.
