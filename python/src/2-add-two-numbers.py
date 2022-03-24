from time import perf_counter

"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        temp = None
        carry = 0

        while l1 is not None or l2 is not None:
            sum_value = carry

            if l1 is not None:
                sum_value += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_value += l2.val
                l2 = l2.next

            node = ListNode(sum_value % 10)
            carry = sum_value // 10

            if temp is None:
                temp = head = node
            else:
                temp.next = node
                temp = temp.next

        if carry > 0:
            temp.next = ListNode(carry)

        return head


def print_node(node):
    res = []
    while node is not None:
        res.append(node.val)
        node = node.next
    print(res)


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    print_node(solution.addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))
    print_node(solution.addTwoNumbers(ListNode(0), ListNode(0)))
    print_node(solution.addTwoNumbers(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))), ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
