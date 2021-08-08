class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1
        
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return h+1
        
        
        while(l<=h):
            m = (l+h) //2
            
            if nums[m] < target:
                l = m+ 1
                
            elif nums[m] > target:
                h = m-1
            elif nums[m] == target:
                return m
            
            elif l ==h:
                return l
        return l
