"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
    Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
    Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
    As long as a house is in the heaters' warm radius range, it can be warmed.
    All the heaters follow your radius standard and the warm radius will the same.

Example 1:
    Input: [1,2,3],[2]
    Output: 1
    Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
    Input: [1,2,3,4],[1,4]
    Output: 1
    Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""


def findRadius(houses: list[int], heaters: list[int]) -> int:
    # 96 ms, faster than 98.77%.
    houses.sort(), heaters.sort()
    dis, start, hp, hl = [], 0, 0, len(heaters)
    while heaters[0] > houses[start]:
        dis.append(heaters[0] - houses[start])
        start += 1
        if start == len(houses):
            return max(dis)
    for h in houses[start:]:
        while hp < hl - 1 and heaters[hp] < h:
            hp += 1
        if heaters[hp] > h:
            dis.append(min(h - heaters[hp - 1], heaters[hp] - h))
            hp -= 1
        else:
            dis.append(h - heaters[hp])
    return max(dis)


def findRadius2(houses: list[int], heaters: list[int]) -> int:
    # 88 ms, faster than 100%. The best solution from submissions.
    houses.sort()
    heaters.sort()
    heaters = [float("-inf")] + heaters + [float("inf")]  # ***
    radius = 0
    # right heater index
    rh_ind = 0
    for house in houses:
        while(house > heaters[rh_ind]):
            rh_ind += 1
        dist = min(house - heaters[rh_ind - 1], heaters[rh_ind] - house)
        if dist > radius:
            radius = dist

    return radius

print(findRadius([617819336,399125485,156091745,356425228],[585640194,937186357]))