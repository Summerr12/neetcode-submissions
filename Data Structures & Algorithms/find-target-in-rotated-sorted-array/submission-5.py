class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if tar > mid
        #     if breakpt is right ( mid > right )

        
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        left=0
        right=len(nums)-1
        
        while left <= right:
            midpt = (left+right) //2
            if nums[midpt] == target: return midpt
           
            print("midpt index: " , midpt , "  val: ", nums[midpt])
            #to know if the rotation was brought to the right side
            if nums[midpt] <= nums[right]: # right half is sorted
                if nums[midpt] < target <= nums[right]:
                    left = midpt + 1
                else:
                    print(2)
                    right = midpt - 1
            else:
                if nums[left] <= target < nums[midpt]:
                    print(4)
                    #look left
                    right = midpt - 1
                else:
                    left = midpt + 1

        return -1
        """
        we have to use the target to decide where to search
        no more is it the smallest or largest value in the list

        thoughts:
        find the break first
        once you find the break, see if the value will require which direction to search

        if break was on the right side, and midpt > target
            target could still be either left or right
            [3,4,5,6,1,2] mid:6 , target 3            

        [2,3,4,5,6,1], target = 6    5 rotations
        >2 >1

        [3,4,5,6,1,2], target = 1
        [4,5,6,1,2,3], target = 1
        [5,6,1,2,3,4]

        breakpt on left half

-----
I think the order of conditions is
side of breakpt
if the edge pt of the side of the breakpt is greater or less than target
compare the midpt


look left = set right to midpt-1
look right = set left to midpt+1
        [3,4,5,6,1,2], target = 1
        [4,5,6,1,2,3]
        if mid > right = breakpt is on the right
            if target > right
                look left
            elif target < right
                look right
            else:
                return index of right
        if mid < right = breakpt is on the left
            if target > left
                look left
            if target < left
                look right
            else:
                return index of left
        else:
            return index of right
        """