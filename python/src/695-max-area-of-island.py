from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water. 

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,
1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,
0,0,0]] Output: 6 Explanation: The answer is not 11, because the island must be connected 4-directionally. 

Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # max_area = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[i])):
        #         if grid[i][j] == 1:
        #             print(i, j)
        #             max_area = max(max_area, self.dfs(grid, i, j))
        # return max_area

        # Love the pythonic way to do this
        return max(self.dfs(grid, i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        return 1 + self.dfs(grid, i - 1, j) + self.dfs(grid, i + 1, j) + self.dfs(grid, i, j - 1) + self.dfs(grid, i, j + 1)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                   [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                   [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
    print(s1)
    assert s1 == 6
    s2 = solution.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]])
    print(s2)
    assert s2 == 0

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
