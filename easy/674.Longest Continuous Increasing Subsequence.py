"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
    Input: [1,3,5,4,7]
    Output: 3
    Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3.
    Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4.

Example 2:
    Input: [2,2,2,2,2]
    Output: 1
    Explanation: The longest continuous increasing subsequence is [2], its length is 1.

Note: Length of the array will not exceed 10,000.
"""


def findLengthOfLCIS(nums: List[int]) -> int:
    # 36 ms, faster than 99.42%. Same as the best solution from submissions (28 ms).
    if not nums:
        return 0
    res, count = 1, 1
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            count += 1
        else:
            if count > res:
                res = count
            count = 1
    return max(res, count)