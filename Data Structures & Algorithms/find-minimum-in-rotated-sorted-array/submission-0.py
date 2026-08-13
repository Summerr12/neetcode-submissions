class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        n ascending array

        """
        if len(nums) == 1: return nums[0]

        min = nums[0]
        for n in nums[1:]:
            if min > n:
                min = n

        return min

        