class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp_2= nums[0]
        dp_1 = max(nums[0],nums[1])
        
        for i in range(2,n):
            dp = max(nums[i]+dp_2, dp_1) #either this plus one prev to prev elemnt or prev element
            dp_2 = dp_1
            dp_1 = dp
        return dp_1