from time import perf_counter

"""
https://leetcode.com/problems/search-insert-position/

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        b = len(nums) - 1
        while a <= b:
            m = (a + b) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                a = m + 1
            else:
                b = m - 1
        return a


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.searchInsert([1, 3, 5, 6], 5))
    print(solution.searchInsert([1, 3, 5, 6], 2))
    print(solution.searchInsert([1, 3, 5, 6], 7))

    print(solution.searchInsert([1, 3, 5, 6], 4))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
