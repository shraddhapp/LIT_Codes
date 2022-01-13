# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        stack = []
        n = 1
        while curr or stack:
            if(curr):
                stack.append(curr)
                curr = curr.left
            else:
                #popped element will be root
                curr = stack.pop()
                if n ==k:
                    return curr.val
                else:
                    n+=1
                    curr=curr.right