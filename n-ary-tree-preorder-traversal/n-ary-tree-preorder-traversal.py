"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
      
        
        def preorder(node):
            ans.append(node.val)
            
            for i in node.children: #recurssion on each child
                preorder(i)
                
        preorder(root)
        return ans