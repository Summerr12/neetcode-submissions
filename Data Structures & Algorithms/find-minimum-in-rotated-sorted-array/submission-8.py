class Solution:
    def findMin(self, nums: List[int]) -> int:


        left = 0
        right = len(nums)-1
        """win condition:
        if prev is larger and right is larger
        if prev < midpt: move right to midpt - 1
        if prev > midpt: move left to midpt
        if next < midpt: move left to midpt + 1, next val must be smallest
        if next > midpt: move right to midpt

        if prev < midpt < next:
        
        if prev > midpt < next: return midpt 
        if left > right: shift left border
        if left < right: shift right border


        
        """
        while left < right:
            midpt = (left + right) //2
            # if midpt > 0 and midpt< len(nums)-1:
            if nums[midpt] > nums[right]:
                left = midpt+1
                print("left")
            # elif nums[left] < nums[right]: 
            else:
                right = midpt
                print("right")
            print("left: ", left, " right: ", right, " midpt: ", midpt)
                

        return nums[left]

        