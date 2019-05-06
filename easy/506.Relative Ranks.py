"""
Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
    Input: [5, 4, 3, 2, 1]
    Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
    Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal".
    For the left two athletes, you just need to output their relative ranks according to their scores.

Note:
    N is a positive integer and won't exceed 10,000.
    All the scores of athletes are guaranteed to be unique.
"""


def findRelativeRanks(nums: List[int]) -> List[str]:
    # 72 ms, faster than 81.89%.
    orders = sorted(nums)[::-1]
    rank = {}
    for order, num in enumerate(orders):
        if order > 2:
            rank[num] = str(order + 1)
        elif order == 0:
            rank[num] = "Gold Medal"
        elif order == 1:
            rank[num] = "Silver Medal"
        else:
            rank[num] = "Bronze Medal"
    return [rank[num] for num in nums]


def findRelativeRanks2(nums: List[int]) -> List[str]:
    # 72 ms, the shortest solution from submissions.
    rank = {n:i>2 and str(i+1) or ["Gold","Silver","Bronze"][i]+' Medal' for i,n in enumerate(sorted(nums,reverse=True))} #*** conditions and operations.
    return [rank[num] for num in nums]


def findRelativeRanks3(nums: List[int]) -> List[str]:
    # 72 ms, the best solution from submissions (60 ms).
    ranks = list(map(str, range(1, len(nums) + 1)))
    ranks[:3] = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
    rating = dict(zip(sorted(nums, reverse=True), ranks))  #  *** zip(iterator, iterator)
    return [rating[n] for n in nums]




print(findRelativeRanks([5, 4, 3, 2, 1]))
print(findRelativeRanks([4]))
a = [1]
print(a[:100])