class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        min heap the list
        while k>0: pop and return pop when k=0
        iterate through whole list
        '''
        heap = [x*-1 for x in nums]
        heapq.heapify(heap)
        while k != 0:
            x = heapq.heappop(heap)
            k-=1
            # print(f"removed {x} from {heap}")

        return -x
