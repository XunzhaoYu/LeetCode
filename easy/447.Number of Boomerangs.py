"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
    Input: [[0,0],[1,0],[2,0]]
    Output: 2
    Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


def numberOfBoomerangs(points: List[List[int]]) -> int:
    # 1000 ms, faster than 85.10%.
    def distance(a, b):
        return (a[0]-b[0])**2+(a[1]-b[1])**2

    res, n_points = 0, len(points)
    counter = [{} for _ in range(n_points)]
    for i in range(n_points):
        for j in range(i+1, n_points):
            dis = distance(points[i], points[j])
            counter[i][dis] = 1 if dis not in counter[i] else counter[i][dis]+1
            counter[j][dis] = 1 if dis not in counter[j] else counter[j][dis]+1
        for n in counter[i]:
            res += counter[i][n] * (counter[i][n]-1)
    return res


def numberOfBoomerangs2(points: List[List[int]]) -> int:
    # 460ms, faster than 99.42%, the best solution from submissions (440 ms).
    ans = 0

    for x1, y1 in points:  # *** access point(x,y) directly. Saves a half time.
        cnts = {}

        for x2, y2 in points:
            dx = x1 - x2
            dy = y1 - y2
            d = dx * dx + dy * dy

            if d in cnts:
                ans += cnts[d]  # *** idea, saves a half time.
                cnts[d] += 1
            else:
                cnts[d] = 1

    return 2 * ans


print(numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))

"""
- 1 1 1 1
1 - 4 2 2
1 4 - 2 2
1 2 2 - 4
1 2 2 4 -
"""