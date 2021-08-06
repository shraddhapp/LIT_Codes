class Solution:
    def romanToInt(self, s: str) -> int:
        t = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        return sum([t[s[i]] if t[s[i]] >= t[s[i+1]] else -t[s[i]] for i in range(len(s)-1)], t[s[-1]])