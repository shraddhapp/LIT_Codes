class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            temp = list(filter(lambda x:x<n,nums))
            ans.append(len(temp))
            
        return ans