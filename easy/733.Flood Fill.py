"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color
as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.
Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
    Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation:
        From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
        by a path of the same color as the starting pixel are colored with the new color.
        Note the bottom corner is not colored 2, because it is not 4-directionally connected
        to the starting pixel.

Note:
    The length of image and image[0] will be in the range [1, 50].
    The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
    The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
"""


def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    # 56 ms, faster than 98.65%. Same as the best solution from submissions(48 ms.)
    old = image[sr][sc]
    if old == newColor:
        return image
    mr, mc = len(image) - 1, len(image[0]) - 1
    queue = [(sr, sc, -1)]
    while queue:
        pr, pc, s = queue.pop(0)
        image[pr][pc] = newColor
        if s != 1 and pr != 0 and image[pr - 1][pc] == old:
            queue.append((pr - 1, pc, 2))
        if s != 2 and pr != mr and image[pr + 1][pc] == old:
            queue.append((pr + 1, pc, 1))
        if s != 3 and pc != 0 and image[pr][pc - 1] == old:
            queue.append((pr, pc - 1, 4))
        if s != 4 and pc != mc and image[pr][pc + 1] == old:
            queue.append((pr, pc + 1, 3))
    return image
