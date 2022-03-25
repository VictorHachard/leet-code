from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):  # 2 is the step
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.singleNumber([2, 2, 1])
    print(s1)
    assert s1 == 1
    s2 = solution.singleNumber([4, 1, 2, 1, 2])
    print(s2)
    assert s2 == 4
    s3 = solution.singleNumber([1])
    print(s3)
    assert s3 == 1

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
