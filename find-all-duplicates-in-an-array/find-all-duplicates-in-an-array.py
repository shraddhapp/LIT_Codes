class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = set()
        for i in nums:
            index = abs(i)-1
            
            if nums[index] < 0:
                result.add(abs(i))
            else:
                nums[index] *= -1
            
        return list(result)