# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
           # print(prev.val,head.val)
          # print(head.val)
        return prev
    

    
    
