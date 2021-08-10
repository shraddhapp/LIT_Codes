class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0
        for i in words:
            cnt = 0
            flag = 0
            
            for j in i:
                if j in allowed:
                    cnt += 1
                if j not in allowed:
                    flag = 1
                    break
            
            if cnt > 0 and flag == 0:
                total +=1
            
        return total