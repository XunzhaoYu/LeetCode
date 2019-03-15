"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums being 2.
    It doesn't matter what you leave beyond the returned length.

Example 2:
    Given nums = [0,1,2,2,3,0,4,2], val = 2,
    Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.
    Note that the order of those five elements can be arbitrary.
    It doesn't matter what values are set beyond the returned length.
"""


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    res = 0
    for i in range(len(nums)):
        if nums[res] == val:
            del nums[res]  # for s in nums: nums.remove(s)   ***
        else:
            res += 1
    return res


def removeElement2(nums, val):
    for i in range(len(nums) - 1, -1, -1):  # ***
        if nums[i] == val:
            del nums[i]
    return len(nums)


test_input = [3, 2, 2, 3]
val = 3
print(removeElement2(test_input, val), test_input)
