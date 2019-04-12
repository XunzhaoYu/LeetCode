"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:
    Input: [3,0,1]
    Output: 2

Example 2:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:
    Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""


def missingNumber(nums: list[int]) -> int:  # 44 ms, faster than 91.85%. Better than the best solution from submissions (36 ms)
    length = len(nums)
    return length * (length + 1) // 2 - sum(nums)


print(missingNumber([9,6,4,2,3,5,7,0,1]))
