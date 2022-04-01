from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/flood-fill/

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from 
the pixel image[sr][sc]. 

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel 
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the 
same color), and so on. Replace the color of all of the aforementioned pixels with newColor. 

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of 
the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel. 

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        else:
            return self.dfs(image, sr, sc, newColor, image[sr][sc])

    def dfs(self, image: List[List[int]], sr: int, sc: int, newColor: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            image[sr][sc] = newColor
            if sr > 0:
                self.dfs(image, sr - 1, sc, newColor, color)
            if sr < len(image) - 1:
                self.dfs(image, sr + 1, sc, newColor, color)
            if sc > 0:
                self.dfs(image, sr, sc - 1, newColor, color)
            if sc < len(image[0]) - 1:
                self.dfs(image, sr, sc + 1, newColor, color)
        return image


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(s1)
    assert s1 == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    s2 = solution.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)
    print(s2)
    assert s2 == [[2, 2, 2], [2, 2, 2]]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
