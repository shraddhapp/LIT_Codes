class Solution:
    def majorityElement(self, num: List[int]) -> int:
        return sorted(num)[len(num)//2]