"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
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
    def maxDepth(self, root: Optional[TreeNode])-> int:

        def recurr(root, depth):
            if not root:
                return depth
            return max(recurr(root.left,depth+1), recurr(root.right,depth+1))

        return recurr(root,0)

#VALID 2
#Binary Tree we want to build root = [3,9,20,null,null,15,7]
r2 = TreeNode(3)
r2.left = TreeNode(9)
r2.right = TreeNode(20)

r2.left.left = TreeNode(None)
r2.left.right = TreeNode(None)

r2.right.left = TreeNode(15)
r2.right.right = TreeNode(7)

c=Solution()
print(c.maxDepth(r2))
print(r2)