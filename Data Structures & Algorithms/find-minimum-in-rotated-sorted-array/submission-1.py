class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        # binary search and at the middle,
        #if the right most value is larger than the midpt, look left
        #if the right is smaller, look right
        #We still need to update mdpt based off left and right cause its positional
        while left < right:
            mdpt = (left+right) // 2
            if nums[mdpt] > nums[right]: # look right
                left = mdpt + 1 
            else: # look right
                right = mdpt
            # print("left", left, " right", right, "midpt: ", mdpt)
        return nums[left]       