from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return
-1.

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens
4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""


class Solution:
    # Stolen solution: https://leetcode.com/problems/rotting-oranges/discuss/1546489/Python-BFS%3A-Easy-to-understand-with-Explanation
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr = set(), []
        # find all fresh and rotten oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
            # BFS iteration
            newr = []
            for i, j in curr:  # obtain recent rotten orange
                for coord in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if coord in visit:  # check if adjacent orange is fresh
                        visit.remove(coord)
                        newr.append(coord)
            curr = newr
            result += 1
        # check if fresh oranges remain and return accordingly
        return -1 if visit else result


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(s1)
    assert s1 == 4
    s2 = solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    print(s2)
    assert s2 == -1
    s3 = solution.orangesRotting([[0, 2]])
    print(s3)
    assert s3 == 0

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
