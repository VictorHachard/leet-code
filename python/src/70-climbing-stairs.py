from time import perf_counter

"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1  # a = 1 step, b = 2 steps
        for i in range(n):
            a, b = b, a + b
        return a


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.climbStairs(2)
    print(s1)
    assert s1 == 2
    s2 = solution.climbStairs(3)
    print(s2)
    assert s2 == 3

    s3 = solution.climbStairs(4)
    print(s3)
    assert s3 == 5
    s4 = solution.climbStairs(38)
    print(s4)
    assert s4 == 63245986

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
