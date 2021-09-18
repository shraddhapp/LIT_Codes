class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a', 'e', 'i', 'o', 'u']
        s=s.lower()
        mid = len(s)//2
        
        firsthalf_count = len([s[i] for i in range(mid) if s[i] in vowels])
        secondhalf_count = len([s[j] for j in range(mid,len(s)) if s[j] in vowels])

        return firsthalf_count==secondhalf_count