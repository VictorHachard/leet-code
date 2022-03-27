from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum 
and return its sum. 

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            result = max(result, nums[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(s1)
    assert s1 == 6
    s2 = solution.maxSubArray([1])
    print(s2)
    assert s2 == 1
    s3 = solution.maxSubArray([5, 4, -1, 7, 8])
    print(s3)
    assert s3 == 23

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
