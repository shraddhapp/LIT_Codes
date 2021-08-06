class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = candies[0]
        
        for i in candies:
            if i>max_c:
                max_c = i
                
        res = [True if j+extraCandies >= max_c else False for j in candies] 
        
        return res