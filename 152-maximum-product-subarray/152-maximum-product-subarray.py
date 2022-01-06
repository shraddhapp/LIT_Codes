class Solution:
    #referred youtube.com/watch?v=tHNsZHXnYd4
    
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        min_n, max_n = ans,ans
        
        for i in range(1,len(nums)):
            if nums[i]<0:
                min_n, max_n = max_n, min_n
                
            max_n = max(nums[i], nums[i]*max_n)
            min_n = min(nums[i], nums[i]*min_n)
            
            ans = max(ans,max_n)
            
        return ans