from time import perf_counter

"""
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of 
your product fails the quality check. Since each version is developed based on the previous version, all the versions 
after a bad version are also bad. 

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following 
ones to be bad. 

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find 
the first bad version. You should minimize the number of calls to the API. 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:

Input: n = 1, bad = 1
Output: 1

Constraints:

1 <= bad <= n <= 231 - 1
"""


class Solution(object):
    # The isBadVersion API is already defined for you.
    # @param version, an integer
    # @return a bool
    def isBadVersion(self, version):
        return version >= 4

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = (start + end) // 2
            if self.isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.firstBadVersion(5))
    print(solution.firstBadVersion(1))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
