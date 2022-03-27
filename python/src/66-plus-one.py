from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the 
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer 
does not contain any leading 0's. 

Increment the large integer by one and return the resulting array of digits.

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = str(digits[0])
        for i in range(1, len(digits)):
            s += str(digits[i])
        return [int(i) for i in str(int(s) + 1)]


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.plusOne([1, 2, 3])
    print(s1)
    assert s1 == [1, 2, 4]
    s2 = solution.plusOne([4, 3, 2, 1])
    print(s2)
    assert s2 == [4, 3, 2, 2]
    s3 = solution.plusOne([9])
    print(s3)
    assert s3 == [1, 0]

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
