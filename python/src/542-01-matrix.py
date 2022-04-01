from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""


class Solution:
    # Help: https://leetcode.com/problems/01-matrix/discuss/363902/BFS-python-explained-and-commneted-(two-approaches)
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        q, v = deque(), set()  # q: queue, v: visited
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    v.add((i, j))

        while q:
            i, j = q.popleft()
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and (x, y) not in v:
                    mat[x][y] = mat[i][j] + 1
                    q.append((x, y))
                    v.add((x, y))

        return mat


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(s1)
    assert s1 == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    s2 = solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    print(s2)
    assert s2 == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
