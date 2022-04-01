from time import perf_counter
from typing import Optional

"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The
binarytree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be
set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to
its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

Follow-up:

You may only use constant extra space.
The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        string = str(self.val)
        if self.left:
            string += '(' + str(self.left) + ')'
        if self.right:
            string += '(' + str(self.right) + ')'
        return string

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root:
            if root.left:
                root.left.next = root.right
            if root.right:
                root.right.next = root.next.left if root.next else None
            self.connect(root.left)
            self.connect(root.right)
        return root


if __name__ == '__main__':
    solution = Solution()
    tic = perf_counter()

    s1 = solution.connect(Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7))))
    print(s1)
    # assert s1 == Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    s2 = solution.connect(Node())
    print(s2)
    # assert s2 == Node()

    toc = perf_counter()
    print(f"Done in {(perf_counter() - tic) * 1000000:0.0f}ms")
