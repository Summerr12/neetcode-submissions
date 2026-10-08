class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        kth = [[]]
        # float() = sqrt((x-0)^2 + (y-0)^2) = sqrt(x^2 + y^2)
        # we can heap a tuple of (dist, coords)
        # while len(kth) < k:
        heap_sum = []
        for i in points:
            sum = math.sqrt((i[0]**2) + (i[1]**2))
            heap_sum.append((sum, i))
        # print(heap_sum)

        heapq.heapify_max(heap_sum)
        while len(heap_sum)>k:
            heapq.heappop_max(heap_sum)
        print(heap_sum)

        heap_sum = list(heap_sum)
        print(heap_sum)

        heap_k = [c for x,c in heap_sum]

        return heap_k
