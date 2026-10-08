class KthLargest:
    '''

    '''
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort()
        #ex: len 8 and k=3, we just do 8-3 to get index 5 where the k 3rd lies
        return self.nums[len(self.nums) - self.k] 
