from time import perf_counter

"""
https://leetcode.com/problems/name/

"""


class Solution:
    def name(self, ):
        pass


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.name("42")
    print(s1)
    assert s1 == 42
    s2 = solution.name("42")
    print(s2)
    assert s2 == 42

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
