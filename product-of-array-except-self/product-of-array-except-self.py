class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #reffered https://www.youtube.com/watch?v=bNvIQI2wAjk
        
        #the product at ith element will be product of all previous elements plus product of all next elements
        
        #in output array compute all prefixes i.e premous prosucts first
        out = [1]*len(nums)
        prev = 1
        for i in range(len(nums)):
            out[i] = prev
            prev *= nums[i]
            
        print(out)
        
        #now for post products keep multiplying prev array with next
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            out[i] *= post
            post *= nums[i]
            
        print(out)
        return (out)