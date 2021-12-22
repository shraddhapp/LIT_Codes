class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            print("In base :" ,nums.copy())
            return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            print("Popped out :",n,"Remained:",nums)
            perms = self.permute(nums)
            
            for perm in perms:
                print("perms now:",perms,"appending:",n)
                perm.append(n)
                
            result.extend(perms)
            print("now result:",result,"appending:",n)
            nums.append(n)
        
        return result