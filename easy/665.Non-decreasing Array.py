"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
    Input: [4,2,3]
    Output: True
    Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
    Input: [4,2,1]
    Output: False
    Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
"""


def checkPossibility(nums: List[int]) -> bool:
    # 40 ms, faster than 99.12%. The best solution from submissions tested to be 44 ms (36 ms).
    one = True
    nl = len(nums)
    for i in range(1, nl):
        if nums[i - 1] > nums[i]:
            if not one:
                return False
            elif i < nl - 1:
                if i > 1 and nums[i - 2] >= nums[i] and nums[i - 1] >= nums[i + 1]:
                    return False
                else:
                    one = False
    return True