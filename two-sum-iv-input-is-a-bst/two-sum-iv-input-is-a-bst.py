# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
   
    
    def convertToArray (self,root: Optional[TreeNode]) -> List:
         
        self.out_list = []
        if root:
            self.out_list+=self.convertToArray(root.left)
            self.out_list.append(root.val)
            self.out_list+=self.convertToArray(root.right) 
        return self.out_list
    
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp = self.convertToArray(root) #Obtain the sorted array
        i,j = 0,len(temp)-1 #Uses two pointer approach
        print(temp)
        
        while i<j:
            if temp[i]+temp[j] == k:
                print(temp[i],temp[j])
                return True
            elif temp[i]+temp[j] < k: #if sum of values of two pointer values is less the move the pointer to next element i.e consider the hier element 
                i+=1
            else:
                j-=1
        
        return False
		