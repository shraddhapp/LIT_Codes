class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        
        for i in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += i
            max_sum = max(curr_sum, max_sum)
        
        return max_sum                