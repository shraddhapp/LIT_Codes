class Solution:
    def minPartitions(self, n: str) -> int:
        n = sorted(n)
        print(n)
        print(n[-1])
        return int(n[-1])
        