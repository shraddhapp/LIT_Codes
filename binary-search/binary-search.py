class Solution:
    
    def bsearch(self, nums: List[int], target: int, low: int, high: int):
        if high < low:
            return -1
            
        mid = (low+high)//2
            
        if target == nums[mid]:
            return mid
        
        if target < nums[mid]:
            return self.bsearch(nums,target,low,mid-1)
        else:
            return self.bsearch(nums,target,mid+1,high)
    
    
    def search(self, nums: List[int], target: int) -> int:
        return self.bsearch(nums, target, 0, len(nums)-1)