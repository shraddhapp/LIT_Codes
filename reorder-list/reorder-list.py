# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def splitList(self,head):
        slow,fast = head,head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
        middle = slow.next
        slow.next = None
        
        return head, middle
        
        
    def reverseList(self,head):
        prev,curr = None,head
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    
    def mergeLists(self,a,b):
        head = a
        while b:
            ta = a.next
            a.next = b
            tb = b.next
            a = ta
            b.next = a
            b = tb
        return head
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        a,b = self.splitList(head)
        #print(a,"\n--------\n",b)
        b = self.reverseList(b)
        #print("-------\n",rev)
        head = self.mergeLists(a,b)
        return head