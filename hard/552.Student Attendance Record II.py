"""
Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:
    'A' : Absent.
    'L' : Late.
    'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

Example 1:
    Input: n = 2
    Output: 8
    Explanation: There are 8 records with length 2 will be regarded as rewardable:
                "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
                Only "AA" won't be regarded as rewardable owing to more than one absent times.

Note: The value of n won't exceed 100,000.
"""
# idea: matrix

def checkRecord(n: int) -> int:
    """
    no_A_XP = A_PP, no_A_PP, no_A_PL
    no_A_PL = A_LP, no_A_LP, no_A_LL
    no_A_LL = A_LP, no_A_LP
    1 no_A_PL(n+1) = no_A_XP(n)
    2 no_A_XP(n+1) = no_A_XP(n) + no_A_PL(n) + no_A_LL(n)
    1 no_A_LL(n+1) = no_A_PL(n)

    A_XP = A_PP, A_PL
    A_PL = A_LP, A_LL
    A_LL = A_LP
    1 A_PL(n+1) = A_XP(n)  # AL
    3 A_XP(n+1) = A_PP(n+1) + A_LP(n+1) + no_A_all(n) # AP LA PA
                = A_XP(n) + A_PL(n) + A_LL(n) + no_A_XX(n)
    0 A_LL(n+1) = A_PL(n)
    """
    # 1076 ms, faster than 41.92%.
    cons, mod = [1, 1, 0, 0, 1, 0], 10 ** 9 + 7
    # cons = [1, 2, 1, 1, 3, 0]
    for i in range(1, n):
        cons = [cons[1], sum(cons[0:3]) % mod, cons[0], cons[4], sum(cons) % mod, cons[3]]
    return sum(cons) % mod


def checkRecord2(n: int) -> int:
    # 60 ms, faster than 100%. The best solution from submissions.
    rs = [[1], [1], [1], [0], [0], [0]]
    base = 10 ** 9 + 7

    def mat_mul(mat1, mat2):
        rs = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        for i in range(len(rs)):
            for j in range(len(rs[0])):
                tmp = 0
                for k in range(len(mat2)):
                    tmp += mat1[i][k] * mat2[k][j]
                rs[i][j] = tmp % base
        return rs

    if n > 1:
        bits = bin(n - 1)[2:][::-1]
        mat = [
            [1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
        ]
        ori = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
        ]
        for c in bits:
            if c == '1':
                ori = mat_mul(ori, mat)
            mat = mat_mul(mat, mat)
        rs = mat_mul(ori, rs)

    return sum([_[0] for _ in rs]) % base