class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChars = set()
        left, res = 0,0
        
        
        for r in range(len(s)):
            while s[r] in uniqueChars:
                uniqueChars.remove(s[left])
                left+=1
            uniqueChars.add(s[r])
            res = max(res,len(uniqueChars))
        
        return res