from collections import defaultdict
from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2
indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"

Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"

Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""


class Solution:
    # Mind-blowing solution from: https://leetcode.com/problems/graph-connectivity-with-threshold/discuss/901419/dsu-python-faster-than-100-of-python3-solutions
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n): self.p = list(range(n))

            def union(self, x, y): self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf, res, m = UF(len(s)), [], defaultdict(list)
        for x, y in pairs:
            uf.union(x, y)
        for i in range(len(s)):
            m[uf.find(i)].append(s[i])
        for comp_id in m.keys():
            m[comp_id].sort(reverse=True)
        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]])
    print(s1)
    assert s1 == "bacd"
    s2 = solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]])
    print(s2)
    assert s2 == "abcd"
    s3 = solution.smallestStringWithSwaps("cba", [[0, 1], [1, 2]])
    print(s3)
    assert s3 == "abc"

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
