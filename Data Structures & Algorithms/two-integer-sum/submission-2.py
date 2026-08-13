class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pool = []
        for i, n in enumerate(nums):
            comp = target-n
            if comp in nums[i+1:]:
                pool.append(i)
                pool.append(nums.index(comp, i+1))
                return pool
        return pool

            