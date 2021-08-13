class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = [first]
        
        for i in encoded:
            first = first ^ i
            ans.append(first)
                
        return ans 