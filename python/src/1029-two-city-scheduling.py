from time import perf_counter
from typing import List

"""
https://leetcode.com/problems/two-city-scheduling/

A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of 
flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti. 

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
 
Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859

Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
"""


class Solution:
    # Stolen from: https://leetcode.com/problems/two-city-scheduling/discuss/297143/Python-faster-than-93-28-ms
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])  # sort by the difference between a and b
        cost = 0
        for i in range(len(costs) // 2):
            cost += costs[i][0] + costs[i + len(costs) // 2][1]
        return cost


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]])
    print(s1)
    assert s1 == 110
    s2 = solution.twoCitySchedCost([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
    print(s2)
    assert s2 == 1859
    s3 = solution.twoCitySchedCost(
        [[515, 563], [451, 713], [537, 709], [343, 819], [855, 779], [457, 60], [650, 359], [631, 42]])
    print(s3)
    assert s3 == 3086

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
