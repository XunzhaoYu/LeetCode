from time import time
"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Note:
    The input array will only contain 0 and 1.
    The length of input array is a positive integer and will not exceed 10,000
"""


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    # 64 ms, faster than 99.03%. Same to the best solution from submissions(60 ms),
    res, count = 0, 0
    for n in nums:
        if n == 1:
            count += 1
        else:
            # res = max(res, count)  # slower
            if count > res:
                res = count
            count = 0
    return max(res, count)


def findMaxConsecutiveOnes2(nums: List[int]) -> int:
    # 1144 ms ???
    nums.append(0)
    res, nums_len, total_len, sec_len = 0, len(nums)-1, 0, 0  # nums.index(0)
    while total_len < nums_len:
        sec_len = nums[total_len:].index(0)
        res = max(res, sec_len)
        total_len += sec_len + 1
    return res

