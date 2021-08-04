class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums = sorted(nums,reverse=True)
        print(nums)
        if len(nums)<4:
            return 0
        else:
            return (nums[0]*nums[1] - nums[-1]*nums[-2])
    