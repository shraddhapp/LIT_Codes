class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Have a dict of word and its freq
        counts = collections.Counter(words)
        
        #get a array wchich will have a tuple of word and count
        heap = [(-count, word) for word, count in counts.items()]
        
        #as default heap structure in python min heap and we want max heap
        # to get top frequent word, we will do a make the counter negative
        #so that the topmost element will come up (i.e -8 < -2 so in min heap -8 will come up wich is actually 8)
        
        heapq.heapify(heap) #creating heap in place
        #by deualt it will sort by fre then word
        
        return [heapq.heappop(heap)[1] for _ in range(k)]