class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        
        
        if (nums[low] <= nums[high-1]):
            print(nums[low])
            return nums[low]
        
        else:
            mid = low+high // 2
            min1= self.findMin(nums[0:mid])
            min2= self.findMin(nums[mid:high])
            return min(min1,min2)