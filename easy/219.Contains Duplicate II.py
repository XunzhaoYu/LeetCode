"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""


def containsNearbyDuplicate(nums, k):  # 80 ms, faster than 28.54%
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    mapping = {}
    for i in range(len(nums)):
        if nums[i] in mapping:
            diff = i - mapping[nums[i]]
            if diff <= k:
                return True
        mapping[nums[i]] = i
    return False


def containsNearbyDuplicate2(nums, k):  # 20 ms, best solution from submissions. But it tested to be 76 ms, faster than 28.84%
    if len(nums) == len(set(nums)):
        return False
    dic = {}

    for i, num in enumerate(nums):  # *** try to use this.
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i

    return False