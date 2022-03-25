from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/squares-of-a-sorted-array/

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in 
non-decreasing order. 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.sortedSquares([-4, -1, 0, 3, 10])
    print(s1)
    assert s1 == [0, 1, 9, 16, 100]
    s2 = solution.sortedSquares([-7, -3, 2, 3, 11])
    print(s2)
    assert s2 == [4, 9, 9, 49, 121]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
