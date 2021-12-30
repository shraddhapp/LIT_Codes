# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow, fast = head, head

        
        while(fast.next!=None and fast!=None and fast.next.next!=None):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        return False