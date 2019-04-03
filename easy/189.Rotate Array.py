"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: [1,2,3,4,5,6,7] and k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: [-1,-100,3,99] and k = 2
    Output: [3,99,-1,-100]
    Explanation:
    rotate 1 steps to the right: [99,-1,-100,3]
    rotate 2 steps to the right: [3,99,-1,-100]

Note:
    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?
"""


def rotate(nums, k):  # intuitive idea: Time Limit Exceed
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    length = len(nums)-1
    for _ in range(k):
        temp = nums[-1]
        for i in range(length, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp


def rotate2(nums, k):  # order change, but used O(n) extra space for "order", and a new list "nums".
    length = len(nums)
    order = [i%length for i in range(length-k, 2*length-k)]
    nums[:] = [nums[i] for i in order]


def rotate3(nums, k):  # solution with O(1) extra space
    def transpose(nums, lo, hi):
        if lo >= hi:
            return
        while lo < hi:
            nums[lo], nums[hi - 1] = (nums[hi - 1], nums[lo])
            lo += 1
            hi -= 1
    length = len(nums)
    k %= length
    transpose(nums, 0, length - k)
    transpose(nums, length - k, length)
    transpose(nums, 0, length)


def rotate4(nums, k):  # fastest method.
    n = len(nums)
    k = k % len(nums)
    nums[:] = nums[n - k:] + nums[:n - k]  # *** nums[:] can change the original nums. see rotate 2
