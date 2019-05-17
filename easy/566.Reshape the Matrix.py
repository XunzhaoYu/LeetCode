"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
    Input:  nums = [[1,2],
                    [3,4]]
            r = 1, c = 4
    Output: [[1,2,3,4]]
    Explanation: The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:
    Input:  nums = [[1,2],
                    [3,4]]
            r = 2, c = 4
    Output: [[1,2],
            [3,4]]
    Explanation: There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
    The height and width of the given matrix is in range [1, 100].
    The given r and c are all positive.
"""


def matrixReshape(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    # 76 ms, faster than 99.92%.
    amount = len(nums) * len(nums[0])
    if r * c != amount:
        return nums
    else:
        res, total = [], []
        for l in nums:
            total += l
        for i in range(r):
            sub = total[i * c:(i + 1) * c]
            res.append(sub)
        return res


def matrixReshape2(nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    # 72 ms, best solution from submissions.
    r_cnt = len(nums)
    c_cnt = len(nums[0])

    if (r_cnt * c_cnt) != (r * c):
        return nums
    else:
        onerow = []
        for i in range(len(nums)):
            onerow += nums[i]
    return [onerow[j*c:(j+1)*c] for j in range(r)]
