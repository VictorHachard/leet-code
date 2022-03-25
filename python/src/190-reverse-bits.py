from time import perf_counter

"""
https://leetcode.com/problems/reverse-bits/

Reverse bits of a given 32 bits unsigned integer.

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output 
will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary 
representation is the same, whether it is signed or unsigned. In Java, the compiler represents the signed integers 
using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the 
output represents the signed integer -1073741825. 

Example 1:

Input: n = 00000010100101000001111010011100 Output:    964176192 (00111001011110000010100101000000) Explanation: The 
input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 
which its binary representation is 00111001011110000010100101000000. 

Example 2:

Input: n = 11111111111111111111111111111101 Output:   3221225471 (10111111111111111111111111111111) Explanation: The 
input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 
which its binary representation is 10111111111111111111111111111111. 

Constraints:

The input must be a binary string of length 32

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    # Stolen solution: https://leetcode.com/problems/reverse-bits/discuss/54932/Three-different-solutions-in-python
    def reverseBits(self, n: int) -> int:
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.reverseBits(43261596)  # 00000010100101000001111010011100
    print(s1)
    assert s1 == 964176192  # 00111001011110000010100101000000

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
