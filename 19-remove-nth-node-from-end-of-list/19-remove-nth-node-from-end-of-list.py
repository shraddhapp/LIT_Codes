# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        prev=head
        while head:
            i = i+1
            head = head.next
        pos = i-n
        if pos<=0:
            if prev and prev.next:
                print(prev)
                prev = prev.next
                return prev
            else:
                return None
        
        head = prev
        
        while pos>1:
            prev = prev.next
            pos = pos-1
        
        if(not prev.next.next):
            front = None
        else:
            front = prev.next.next
            
        prev.next = front
        
        return head
        