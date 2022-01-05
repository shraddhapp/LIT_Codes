class Solution:
    def isPalindrome(self, s: str) -> bool:
        s =s.lower()
        str_n = ''.join(filter(str.isalnum,s))
        
        l = 0
        e = len(str_n)-1
        
        while(l<e):
            if str_n[l] != str_n[e]:
                return False
            l+=1
            e-=1
        
        return True