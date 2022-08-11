"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Method to show the TreeNode in the results
    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)

class Solution:
    def minDepth(self, root:Optional[TreeNode])-> int:

        if not root:
            return 0

        left  = 1 + self.minDepth(root.left)
        right = 1 + self.minDepth(root.right)

        if left == 1:
            left = right
        elif right == 1:
            right = left

        return min(left,right)
