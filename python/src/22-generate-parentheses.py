from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.generateParenthesis(3)
    print(s1)
    assert s1 == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    s2 = solution.generateParenthesis(1)
    print(s2)
    assert s2 == ["()"]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
