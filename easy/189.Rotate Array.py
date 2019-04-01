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


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    """ # intuitive idea: Time Limit Exceed
    length = len(nums)-1
    for _ in range(k):
        temp = nums[-1]
        for i in range(length, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = temp
    """
    """ # order change, but used O(n) extra space for "order", and a new list "nums".
    length = len(nums)
    order = [i%length for i in range(length-k, 2*length-k)]
    nums = [nums[i] for i in order]
    """
    length = len(nums)

    index_in, index_out = 0, length - k
    temp = nums[index_in]
    while index_out != 0:
        nums[index_in] = nums[index_out]
    index_out = index_in
    index_in = index_in - k
    if index_in < 0:
        index_in += length
