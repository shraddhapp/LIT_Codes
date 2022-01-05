class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0]*26
            
            for c in s:
                pos = ord(c) - ord('a')
                count[pos] +=1
                
            ans[tuple(count)].append(s)
            
        return ans.values()
 
    