class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        a = [0]*(n+1)
        print(n)
        a[n] = 1
        print(n-1)
        a [n-1] = 1
        print(n-2)
        n = n-2
        while(n>=0):
            print(n,n+1,n+2)
            a[n] = a[n+1] + a[n+2]
            n = n-1
            
        return a[0]