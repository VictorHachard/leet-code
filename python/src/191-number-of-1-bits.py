from time import perf_counter

"""
https://leetcode.com/problems/number-of-1-bits/

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a
signed integer type. It should not affect your implementation, as the integer's internal binary representation is the
same, whether it is signed or unsigned.

In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input
represents the signed integer. -3.

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:

The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")

    # Stolen solution: https://leetcode.com/problems/number-of-1-bits/discuss/644682/Easy-to-Understand-or-Faster-than-98-or-2-solutions-or-Simple-or-Python
    def usingBitManipulation(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.hammingWeight(11)  # 00000000000000000000000000001011
    print(s1)
    assert s1 == 3
    s2 = solution.hammingWeight(128)  # 00000000000000000000000010000000
    print(s2)
    assert s2 == 1
    s3 = solution.hammingWeight(4294967293)  # 11111111111111111111111111111101
    print(s3)
    assert s3 == 31


    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
