class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        prev = self.getRow(rowIndex - 1)
        ans = []
        ans.append(1)
        for i in range(0, len(prev) - 1):
            ans.append(prev[i] + prev[i+1])
        ans.append(1)
        
        return ans