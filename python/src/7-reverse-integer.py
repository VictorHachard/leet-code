from time import perf_counter

"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""


class Solution:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    def reverse(self, x: int) -> int:
        if x < 0:
            result = -self.reverse(-x)
            return result if self.INT_MAX >= result >= self.INT_MIN else 0
        else:
            # same as: 9-palindrome-number.py
            result = 0
            while x > 0:
                result = result * 10 + x % 10
                x //= 10
            # If we are in recursion, this check is not necessary.
            return result if self.INT_MAX >= result >= self.INT_MIN else 0


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))

    print(solution.reverse(1534236469))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
