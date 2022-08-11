from typing import Optional
class ListNode:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self,val=0,next=None):
        self.head = None
        self.val = val
        self.next = next
    def insert(self, data):
        newNode = ListNode(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

#LinkedList with a single node

#Creating a node
LL1 = LinkedList()
LL1.insert(1)
LL1.insert(2)
LL1.insert(4)
#LL.printLL()
LL2 = LinkedList()
LL2.insert(1)
LL2.insert(2)
LL2.insert(5)

class Solution:
    def mergeTwoLists(self, list1: Optional[LinkedList], list2: Optional[LinkedList]) -> Optional[LinkedList]:
        cur = dummy = LinkedList()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next
#Testing a ListNode with more than 1 node
#x = LL1.head
#while x:
#    print(x.data)
#    x = x.next
#Merging List nodes
c = Solution()
x = c.mergeTwoLists(LL1,LL2)
while x:
    print(x.val)
    x = x.next
