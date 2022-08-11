from typing import Optional
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = prev = head

        while node:
            print(f'One round')
            if prev.val == node.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head

#Validation
head = ListNode([1,1,2])
c = Solution()
print(c.deleteDuplicates(head))