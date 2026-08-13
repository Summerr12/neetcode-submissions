class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4,5]
        #[1,1,1,1,1]
        #[1,1,1*2,1*2*3, 1*2*3*4]
        #[1*5*4*3*2,1*5*4*3,1*2*5*4,1*2*3*5, 1*2*3*4]
        #fill a list with 1s based off length of list
        #then multiply the value we are currently iterated on to the list
        #then increment to the next value and multiply it to the entire list except its current position
        totals = [1] * len(nums)
        temp = 1
        for i in range(len(nums)):
            totals[i] *= temp
            temp *= nums[i]
            
        
        temp = 1
        for i in reversed(range(len(nums))):
            totals[i] *= temp
            temp *= nums[i]

        return totals        