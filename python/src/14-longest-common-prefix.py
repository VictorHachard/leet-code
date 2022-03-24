from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pass


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
