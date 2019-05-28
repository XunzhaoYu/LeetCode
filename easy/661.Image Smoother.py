"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
    Input:
        [[1,1,1],
         [1,0,1],
         [1,1,1]]
    Output:
        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    Explanation:
        For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
        For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
        For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
    The value in the given matrix is in the range of [0, 255].
    The length and width of the given matrix are in the range of [1, 150].
"""

def imageSmoother(M: List[List[int]]) -> List[List[int]]:
    # 260 ms, faster than 100%. The best solution from submissions is 296 ms.
    R, C = len(M), len(M[0])
    # special cases:
    if R < 3 and C < 3:
        s = sum([sum(L) for L in M])
        return [[s // (R * C)] * C for _ in M]
    if R == 1:
        return [[(M[0][0] + M[0][1]) // 2] + [(M[0][i] + M[0][i + 1] + M[0][i + 2]) // 3 for i in range(C - 2)] + [(M[0][-2] + M[0][-1]) // 2]]
    if C == 1:
        return [[(M[0][0] + M[1][0]) // 2]] + [[(M[i][0] + M[i + 1][0] + M[i + 2][0]) // 3] for i in range(R - 2)] + [[(M[-2][0] + M[-1][0]) // 2]]

    # common cases:
    Rl, Cl = R - 1, C - 1
    ans = [[0] * C for _ in M]

    ass = [[0] * (C) for _ in M]
    for r in range(R):
        ass[r][0] = M[r][0] + M[r][1]
        ass[r][Cl] = M[r][Cl] + M[r][Cl - 1]
        for c in range(1, Cl):
            ass[r][c] = M[r][c - 1] + M[r][c] + M[r][c + 1]

    for c in [0, Cl]:
        ans[0][c] = (ass[0][c] + ass[1][c]) // 4
        ans[Rl][c] = (ass[Rl][c] + ass[Rl - 1][c]) // 4
        for r in range(1, Rl):
            ans[r][c] = (ass[r - 1][c] + ass[r][c] + ass[r + 1][c]) // 6
    for c in range(1, Cl):
        ans[0][c] = (ass[0][c] + ass[1][c]) // 6
        ans[Rl][c] = (ass[Rl][c] + ass[Rl - 1][c]) // 6
        for r in range(1, Rl):
            ans[r][c] = (ass[r - 1][c] + ass[r][c] + ass[r + 1][c]) // 9

    return ans