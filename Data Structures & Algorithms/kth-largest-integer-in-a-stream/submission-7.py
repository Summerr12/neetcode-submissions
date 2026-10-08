class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

    #non heap version
    # def __init__(self, k: int, nums: List[int]):
    #     self.k = k
    #     self.nums = sorted(nums)[-k:] # keeps only kth largest and up
        

    # def add(self, val: int) -> int:
    #     # if there is a change in the right region of list, update
    #     if len(self.nums) < self.k: # fill k requirement because k can be greater than length of list
    #         self.nums.append(val)
    #         self.nums.sort()
    #     elif val> self.nums[0]:
    #         self.nums.append(val)
    #         self.nums.sort()
    #         self.nums.pop(0)
        
    #     return self.nums[0]
