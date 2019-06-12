"""
n a given integer array nums, there is always exactly one largest element.
Find whether the largest element in the array is at least twice as much as every other number in the array.
If it is, return the index of the largest element, otherwise return -1.

Example 1:
    Input: nums = [3, 6, 1, 0]
    Output: 1
    Explanation: 6 is the largest integer, and for every other number in the array x,
    6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

Example 2:
    Input: nums = [1, 2, 3, 4]
    Output: -1
    Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Note:
    nums will have a length in the range [1, 50].
    Every nums[i] will be an integer in the range [0, 99].
"""


def dominantIndex(nums):# List[int]) -> int:  comparision: 2N
    # 32 ms, faster than 96.12%
    res, nl = 0, len(nums)
    smax, fmax = -1, nums[0]
    for i in range(1, nl):
        if nums[i] > smax:
            if nums[i] > fmax:
                smax = fmax
                fmax = nums[i]
                res = i
            elif nums[i] < fmax:
                smax = nums[i]
    return res if fmax >= 2*smax else -1


def dominantIndex2(nums):# List[int]) -> int:
    # 32 ms, the best solution from submissions (20 ms). comparision: N~2N
    if not nums:
        return -1
    largest = max(nums)
    largest_idx = nums.index(largest)
    nums.remove(largest)
    for x in nums:
        if 2 * x > largest:
            return -1
        else:
            pass
    return largest_idx


