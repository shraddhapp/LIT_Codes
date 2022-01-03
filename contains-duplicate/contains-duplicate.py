class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        
        return False if len(set_nums) == len(nums) else True