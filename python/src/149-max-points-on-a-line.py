from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of
points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = (points[0][0] - points[-1][0]) / (points[0][1] - points[-1][1])
        b = points[0][0] - m * points[0][1]


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.maxPoints([[1, 1], [2, 2], [3, 3]])
    print(s1)
    assert s1 == 3
    s2 = solution.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
    print(s2)
    assert s2 == 4

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
