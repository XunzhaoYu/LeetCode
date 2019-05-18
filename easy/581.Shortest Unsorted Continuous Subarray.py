"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
    Input: [2, 6, 4, 8, 10, 9, 15]
    Output: 5
    Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Note:
    Then length of the input array is in range [1, 10,000].
    The input array may contain duplicates, so ascending order here means <=.
"""


def findUnsortedSubarray(nums: List[int]) -> int:
    # 60 ms, faster than 96.62%. The best one is 48 ms.
    s_nums, n_nums = sorted(nums), len(nums)
    fp, lp = n_nums, n_nums-1
    for i in range(n_nums):
        if s_nums[i] != nums[i]:
            fp = i
            break
    if fp == n_nums:
        return 0
    for i in range(lp, 0, -1):
        if s_nums[i] != nums[i]:
            lp = i
            break
    return lp - fp + 1


def findUnsortedSubarray2(nums: List[int]) -> int:
    # 52 ms, faster than 99.94%. Best solution from submissions (48 ms)
    i, j = 0, len(nums) - 1
    while i < j and nums[i] <= nums [i+1]: i += 1
    if i >= j:
        return (0)
    while j > 0 and nums[j] >= nums[j-1]: j -= 1

    max_sub, min_sub = max(nums[i:j+1]), min(nums[i:j+1])

    while i >= 0 and nums[i] > min_sub: i -= 1

    while j <= len(nums) - 1 and  nums[j] < max_sub: j += 1

    return(j-i-1)