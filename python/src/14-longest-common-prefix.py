from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


class Solution:
    # Stolen solution: https://leetcode.com/problems/longest-common-prefix/discuss/1858866/python3-o(n)-Solution-faster-than-95-user-and-90-less-space-usage
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        shortest, longest = min(strs), max(strs)
        print(shortest, longest)
        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                result += shortest[i]
            else:
                break
        return result



if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
    print(solution.longestCommonPrefix(["dog", "racecar", "car"]))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
