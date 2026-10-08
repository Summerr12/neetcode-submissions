class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #looks like sliding window 
        #choosing the heaviest 2 rocks
        maxHeap = stones
        heapq.heapify_max(maxHeap)
        
        while len(maxHeap) > 1:
            x = heapq.heappop_max(maxHeap)
            y = heapq.heappop_max(maxHeap)
            xy = abs(x-y)
            heapq.heappush_max(maxHeap, xy)

        return maxHeap[0]