from time import perf_counter

"""
https://leetcode.com/problems/power-of-two/

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:

Input: n = 3
Output: false

Constraints:

-231 <= n <= 231 - 1
"""


class Solution:
    # Mind-blowing solution from: https://leetcode.com/problems/power-of-two/discuss/948641/Python-O(1)-Solution
    def isPowerOfTwo(self, n: int) -> bool:
        return 0 < n == (n & -n)  # n > 0 and n & (n-1) == 0


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.isPowerOfTwo(1)
    print(s1)
    assert s1
    s2 = solution.isPowerOfTwo(16)
    print(s2)
    assert s2
    s3 = solution.isPowerOfTwo(3)
    print(s3)
    assert not s3

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
