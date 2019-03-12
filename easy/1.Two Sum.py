"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
"""


def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    find = False
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            sum = nums[i] + nums[j]
            if sum == target:
                result = [i, j]
                find = True
                break
        if find:
            break
    return result


def twoSum2(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i
        else:
            return [map[num[i]], i]


nums = [2, 7, 11, 15]
target = 9
print(twoSum2(nums, target))
