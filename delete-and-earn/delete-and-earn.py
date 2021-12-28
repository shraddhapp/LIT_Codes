class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #Refered = https://www.youtube.com/watch?v=7FCemBxvGw0
        
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        
        e1, e2 = 0,0
        
        for i in range(len(nums)):
            currEarning = nums[i] * count[nums[i]]
            
            if (i>0) and (nums[i] == nums[i-1]+1):
                t = e2
                e2 = max(currEarning + e1, e2)
                e1 = t
            else:
                t = e2
                e2 = currEarning + e2
                e1 = t
            
        return e2