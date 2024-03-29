"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Given nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the returned length.

Example 2:
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
    It doesn't matter what values are set beyond the returned length.
"""


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    if length < 2:
        return length
    res = 1
    for index in range(1, length):
        if nums[index - 1] != nums[index]:
            nums[res] = nums[index]  # del nums[index] or nums.pop(index) also works ***
            res += 1
    return res


def removeDuplicates2(nums):
    nums[:] = list(set(nums))  # ***
    nums.sort()
    return(len(nums))


test_input = [1, 1, 2]
print(removeDuplicates(test_input), test_input)
test_input2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(test_input2), test_input2)