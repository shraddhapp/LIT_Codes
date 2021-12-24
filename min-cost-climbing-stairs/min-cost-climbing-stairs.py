#Reffered https://www.youtube.com/watch?v=ktmzAZWkEZ0&t=566s
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        cost.append(0)
        n = len(cost)
        for i in range(n-3,-1,-1):
            cost[i]+=min(cost[i+2],cost[i+1])
            print(cost[i])
            
        return min(cost[0],cost[1])