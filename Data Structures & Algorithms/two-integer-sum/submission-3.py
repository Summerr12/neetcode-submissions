class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            comp = target-n
            if comp in nums[i+1:]:
                return [i,nums.index(comp, i+1)]
        return []

            