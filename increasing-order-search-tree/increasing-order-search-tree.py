# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        arr=list()
        
        def in_order(root,arr):
            if root:
                in_order(root.left,arr)
                arr.append(root.val)
                in_order(root.right,arr)
                
            dummy=TreeNode()
            root=dummy
            
            for i in arr:
                root.right=TreeNode(i)
                root=root.right
            return dummy.right
                                  
        return in_order(root,list(arr))