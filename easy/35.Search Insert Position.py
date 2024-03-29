"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start, end = 0, len(nums)
    while start < end:
        mid = (start+end)//2
        if nums[mid] > target:
            end = mid
        elif nums[mid] < target:
            start = mid+1
        else:
            return mid
    return start


test_input_argu1 = [1, 3, 5, 6]
test_input_argu2 = 5
print(searchInsert(test_input_argu1, test_input_argu2))
test_input_argu2 = 2
print(searchInsert(test_input_argu1, test_input_argu2))
test_input_argu2 = 7
print(searchInsert(test_input_argu1, test_input_argu2))
test_input_argu2 = 0
print(searchInsert(test_input_argu1, test_input_argu2))