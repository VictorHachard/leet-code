from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:

Input: nums = [1,2,0]
Output: 3

Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.firstMissingPositive([1, 2, 0])
    print(s1)
    assert s1 == 3
    s2 = solution.firstMissingPositive([3, 4, -1, 1])
    print(s2)
    assert s2 == 2
    s3 = solution.firstMissingPositive([7, 8, 9, 11, 12])
    print(s3)
    assert s3 == 1

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
