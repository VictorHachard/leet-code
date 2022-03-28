from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money 
stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems 
connected and it will automatically contact the police if two adjacent houses were broken into on the same night. 

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you 
can rob tonight without alerting the police. 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    # Stolen solution: https://leetcode.com/problems/house-robber/discuss/55977/Python-DP-solution-4-line-O(n)-time-O(1)-space-easy-to-understand-with-detailed-explanation
    def robEasy(self, nums: List[int]) -> int:
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in nums:
            max_3_house_before, max_2_house_before, adjacent =\
                max_2_house_before, adjacent, max(max_3_house_before + cur, max_2_house_before + cur)
        return max(max_2_house_before, adjacent)

    # Stolen solution: https://leetcode.com/problems/house-robber/discuss/55696/Python-solution-3-lines.
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.rob([1, 2, 3, 1])
    print(s1)
    assert s1 == 4
    s2 = solution.rob([2, 7, 9, 3, 1])
    print(s2)
    assert s2 == 12

    s3 = solution.rob([1, 2, 3, 1, 1, 3])
    print(s3)
    assert s3 == 7
    s4 = solution.rob([2, 7, 9, 3, 1, 1, 1])
    print(s4)
    assert s4 == 13
    s5 = solution.rob([2, 2, 9, 2, 1, 10])
    print(s5)
    assert s5 == 21

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
