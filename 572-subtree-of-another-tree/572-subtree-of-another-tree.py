# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True #empty subtree is subset of tree
        if not root: return False #if subset is there but tree is not
        
        
        if self.isSameTree(root,subRoot):
            return True
        
        return(self.isSubtree(root.left,subRoot) or #check in every branch
              self.isSubtree(root.right,subRoot))
        
        
    def isSameTree(self,a,b):
        if not a and not b:
            return True
        
        if a and b and a.val == b.val:
            return(self.isSameTree(a.left,b.left) and
                  self.isSameTree(a.right,b.right))
        
        else:
            return False
            
        