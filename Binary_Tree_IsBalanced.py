from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def numberOfLeafs(root, leaf):
            # print(f"root left = {root.left}\n root right = {root.right}")
            if not root:
                return leaf
            else:
                # print(f"veio pro else")
                leaf += 1
                return max(numberOfLeafs(root.left, leaf), numberOfLeafs(root.right, leaf))

        if not root:
            return True

        rootRight = numberOfLeafs(root.left, 0)
        rootLeft = numberOfLeafs(root.right, 0)

        return self.isBalanced(root.left) and \
               self.isBalanced(root.right) and \
               abs(rootLeft - rootRight) < 2



#Correct Solution of Discussion Session of Leetcode==================================================================================
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height_of_tree(root: TreeNode) -> int:
            if not root:
                return 0

            return max(height_of_tree(root.left), height_of_tree(root.right)) + 1

        if not root:
            return True

        return self.isBalanced(root.left) and \
               self.isBalanced(root.right) and \
               abs(height_of_tree(root.left) - height_of_tree(root.right)) <= 1


#Valid====================================================================================================
Sol = Solution()
a7 = TreeNode(7)
a15 = TreeNode(15)

root = [3,9,20,None,None,15,7]
a=TreeNode(20,a15,a7)
b=TreeNode(9,None,None)
c=TreeNode(3,b,a)
print(c)
print(Sol.isBalanced(c))

root = [1,2,2,3,3,None,None,4,4]
a4 = TreeNode(4,None, None)
a3 = TreeNode(3,None,None)
a2 = TreeNode(2,None,None)
a344 = TreeNode(3,a4,a4)
a233 = TreeNode(2,a344,a3)
a1234 = TreeNode(1, a233, a2)

print(a1234)
print(Sol.isBalanced(a1234))

root = [1,None,2,None,3]
a4 = TreeNode(4,None, None)
a3 = TreeNode(3,None,None)
a2 = TreeNode(2,None,None)
a344 = TreeNode(3,a4,a4)
a233 = TreeNode(2,a344,a3)
a1234 = TreeNode(1, a233, a2)


