class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(len(intervals)<2):
            return intervals
        intervals.sort()
        output=[intervals[0]]
        for start,end in intervals[1:]:
            if(start>output[-1][1]):
                output.append([start,end])
            elif(end>output[-1][1]):
                output[-1][1]=end
        return output