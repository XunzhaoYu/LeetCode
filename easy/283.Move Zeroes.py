"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""


def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 48 ms, faster than 79.89%, same to the best solution from submissions(40 ms)
    moved_index = 0
    for index, number in enumerate(nums):
        if number != 0:
            nums[moved_index] = number
            moved_index += 1
    nums[moved_index:] = [0] * (len(nums) - moved_index)
