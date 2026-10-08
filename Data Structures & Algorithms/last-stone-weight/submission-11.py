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

        #not heap
        # stones.sort(reverse = True)
        # while len(stones) > 1:
        #     xy = abs(stones[0] - stones[1])
        #     stones.append(xy)
        #     stones = stones[2:]
        #     stones.sort(reverse = True)

        # return stones[0]