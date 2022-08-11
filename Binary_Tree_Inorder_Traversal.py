from typing import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    #Method to show the TreeNode in the results
    def __repr__(self) -> str:
        return '[%s, %r, %r]' % (self.val, self.left, self.right)

class Solution:
    def inorderTraversal(self, root:Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        inorder(root)
        return result

n2 = TreeNode(2,3,None)
n1 = TreeNode(1,None,n2)
c = Solution()
print(c.inorderTraversal(n1))