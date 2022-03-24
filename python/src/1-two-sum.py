from time import perf_counter

"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        map = {}

        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            if target - nums[i] in map and map[target - nums[i]] != i:
                output.append(i)
                output.append(map[target - nums[i]])
                return output


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
