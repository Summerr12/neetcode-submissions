class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            midpt = (left + right) //2
            if nums[midpt] > nums[right]:
                left = midpt+1
            else:
                right = midpt
            # print("left: ", left, " right: ", right, " midpt: ", midpt)
                
        return nums[left]

        