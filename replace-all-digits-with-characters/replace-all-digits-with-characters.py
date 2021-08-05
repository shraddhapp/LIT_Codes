class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift( x, y) ->int:
            return chr(int(x)+ord(y))
        
        ans = ""
        
        for i in range(len(s)):
            if s[i].isdigit():
                ans+=(shift(s[i],s[i-1]))
            else:
                ans+=s[i]
                
        return ans