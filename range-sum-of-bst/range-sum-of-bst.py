# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        out = self.cal(root, low, high, 0)
        return out
    
    def cal(self, root, low, high, ans):
            if root:
                if root.val >= low and root.val <= high:
                    ans+=root.val
                ans = self.cal(root.left,low,high,ans)
                ans = self.cal(root.right,low,high,ans)
            return ans
                