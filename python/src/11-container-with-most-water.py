from time import perf_counter

"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7] Output: 49 Explanation: The above vertical lines are represented by array [1,8,6,
2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""


class Solution(object):
    # Stolen solution: https://leetcode.com/problems/container-with-most-water/discuss/1868783/Python-With-Best-Explanation
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        max_amount = 0

        # Test whether it's worth sacrificing width (narrowing the basin) to gain height (finding a taller side bar)
        # by moving the shorter of the two bars at L and R towards the other until a taller bar is found, or exit the
        # loop when the sides meet.
        while l < r:
            hl, hr = height[l], height[r]
            max_amount = max(max_amount, min(hl, hr) * (r - l))
            if hl < hr:
                l += 1
                while l < r and height[l] <= hl:
                    l += 1
            else:
                r -= 1
                while l < r and height[r] <= hr:
                    r -= 1
        return max_amount


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(solution.maxArea([1, 1]))

    print(solution.maxArea([1, 2]))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
