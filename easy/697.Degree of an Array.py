"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation:
        The input array has a degree of 2 because both elements 1 and 2 appear twice.
        Of the subarrays that have the same degree:
        [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
        The shortest length is 2. So return 2.

Example 2:
    Input: [1,2,2,3,1,4,2]
    Output: 6

Note:
    nums.length will be between 1 and 50,000.
    nums[i] will be an integer between 0 and 49,999.
"""


def findShortestSubArray(nums: List[int]) -> int:
    # 76 ms, faster than 86.42%.  
    dic, degree, num, res = {}, 1, nums[0], 0
    for i, n in enumerate(nums):
        if n not in dic:
            dic[n] = [1, i, i]
        else:
            temp = dic[n][0] + 1
            dic[n][0] = temp
            dic[n][2] = i
            if temp > degree:
                degree, num, res = temp, n, i - dic[n][1]
            elif temp == degree:
                length = i - dic[n][1]
                if length < res:
                    num, res = n, length
    return res + 1


def findShortestSubArray(nums: List[int]) -> int:
    # 40 ms, best solution from submissions.
    if len(nums) == len(set(nums)):
        return 1

    # Find degree of nums
    from collections import Counter
    numsCounter = Counter(nums)
    degree = max(numsCounter.values())
    maxFreqEle = []

    # Find elements with frequency = degree
    for x in numsCounter.keys():
        if numsCounter[x] == degree:
            maxFreqEle.append(x)

    # Find min distance elements with frequency = degree
    l = len(nums) - 1
    minDist = l + 1
    for x in maxFreqEle:
        start = nums.index(x)
        for i in range(l, -1, -1):
            if nums[i] == x:
                end = i
                break
        minDist = min(end - start + 1, minDist)

    return minDist