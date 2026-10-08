class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        # float() = sqrt((x-0)^2 + (y-0)^2) = sqrt(x^2 + y^2)
        # we can heap a tuple of (dist, coords)
        # while len(kth) < k:
        for x,y in points:
            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(heap, (-dist, [x,y]))
        # print(heap_sum)
            if len(heap) > k:
                heapq.heappop(heap)

        return [c for _,c in heap]
