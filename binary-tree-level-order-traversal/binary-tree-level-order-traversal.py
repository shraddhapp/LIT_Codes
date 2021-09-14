# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#ref:  https://www.youtube.com/watch?v=MBZ-gBkjdMc


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = [root]
        nextqueue, temp, res = [], [] ,[]

        
        while queue!=[]:
            for root in queue:
                temp.append(root.val)
                if root.left:
                    nextqueue.append(root.left)
                if root.right:
                    nextqueue.append(root.right)
            res.append(temp)
            queue = nextqueue
            temp, nextqueue = [], []
            
        return res
        