from time import perf_counter

"""
https://leetcode.com/problems/defanging-an-ip-address/

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]". 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:

The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.defangIPaddr("1.1.1.1")
    print(s1)
    assert s1 == "1[.]1[.]1[.]1"
    s2 = solution.defangIPaddr("255.100.50.0")
    print(s2)
    assert s2 == "255[.]100[.]50[.]0"

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
