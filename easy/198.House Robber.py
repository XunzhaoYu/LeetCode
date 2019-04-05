"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
    Input: [1,2,3,1]
    Output: 4
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.

Example 2:
    Input: [2,7,9,3,1]
    Output: 12
    Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""


def rob(nums):  # 20 ms, faster than 72.21%
    """
    :type nums: List[int]
    :rtype: int
    """
    houses = len(nums)
    res3, res2, res1 = 0, 0, 0
    for i in range(houses):
        res = nums[i] + max(res3, res2)
        res3, res2, res1 = res2, res1, res
    return max(res2, res1)


def rob2(nums):  # 20 ms, faster than 72.21%, best solution from submissions.
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
    return dp[-1]
