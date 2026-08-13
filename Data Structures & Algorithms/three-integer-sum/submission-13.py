class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        nums=[-1,0,1,2,-1,-4]
        sort nums
        nums = [-4,-1,-1,0,1,2]

        left ptr
        right ptr
        curr

        starting at -4
        that means we need to look for a 2 values to equate to 4
        so starting at each end of the list after -4
        if -1 + 2 < 4:
            increase the left num so we get a larger total
            by looping left to right
            if we find a match, append
        if -1 + 2 > 4
            decrease the right num so we get a smaller total
            by looping righ to left
            if we find a match, append
        after match or no match, we increment the target

        """

        r = []
        nums.sort()

        for i in range(len(nums)): #0, 1, 5 len 6
            curr = nums[i]
            j = i+1
            k = len(nums)-1
            while j < k:
                # print(f"we have: i:{i} j:{j} k:{k} LF {-(curr)}")
                left = nums[j]
                right = nums[k]
                if left + right < -(curr): #shift left value to right
                    j+=1
                elif left + right > -(curr): #shift right value to left
                    k-=1
                else:
                    if [left, curr, right] not in r:
                        r.append([left, curr, right])
                    # j+=1
                    k-=1
                    # print(left, curr, right)
                    
        return r
