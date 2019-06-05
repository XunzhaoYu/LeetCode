""" day 82, 2, 31th May
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Note:
    You may assume that all elements in nums are unique.
    n will be in the range [1, 10000].
    The value of each element in nums will be in the range [-9999, 9999].
"""


def search(nums: List[int], target: int) -> int:
    # 44 ms, faster than 94.51%. Same as the best solution from submissions (32 ms)
    start, end = 0, len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            return mid
    return -1
