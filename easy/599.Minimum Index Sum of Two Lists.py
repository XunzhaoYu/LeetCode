"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    Output: ["Shogun"]
    Explanation: The only restaurant they both like is "Shogun".

Example 2:
    Input:
    ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    ["KFC", "Shogun", "Burger King"]
    Output: ["Shogun"]
    Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
    The length of both lists will be in the range of [1, 1000].
    The length of strings in both lists will be in the range of [1, 30].
    The index is starting from 0 to the list length minus 1.
    No duplicates in both lists.
"""


def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    # 64 ms, faster than 93.16%.
    res, min_sum, dic1, dic2 = [], float('inf'), {}, {}
    for i, r in enumerate(list1):
        dic1[r] = i
    for i, r in enumerate(list2):
        if r in dic1:
            temp = i + dic1[r]
            if min_sum > temp:
                min_sum = temp
                res = [r]
            elif min_sum == temp:
                res.append(r)
    return res


def findRestaurant2(list1: List[str], list2: List[str]) -> List[str]:
    # 48 ms, faster than 100%. The best solution from submissions.
    res = []
    res_val = 2001
    dict1 = {k:v for v,k in enumerate(list1)}  # ***

    for v1,k1 in enumerate(list2):
        if v1 > res_val:
            break
        v = dict1.get(k1, 2001)  # ***
        if v1+v < res_val:
            res = [k1]
            res_val =v1+v
        elif v1+v == res_val:
            res.append(k1)
    return res
