"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
    Input: [1,12,-5,-6,50,3], k = 4
    Output: 12.75
    Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:
    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].
"""


def findMaxAverage(nums: List[int], k: int) -> float:
        # 120 ms, faster than 100.00%.
        res, diff = sum(nums[:k]), 0
        for i in range(k, len(nums)):
            diff += nums[i] - nums[i-k]
            if diff > 0:
                res += diff
                diff = 0
        return res/k