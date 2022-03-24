from time import perf_counter

"""
https://leetcode.com/problems/

"""


class Solution:
    def name(self, ):
        pass


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.name())
    print(solution.name())
    print(solution.name())

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
