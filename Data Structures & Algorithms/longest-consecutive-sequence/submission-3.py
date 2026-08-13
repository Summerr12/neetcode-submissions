class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0
        if len(nums) == 0: return 0

        sorted_set = sorted(set(nums)) #sort into set
        best_count = 1 # initialize base count

        for i in sorted_set: #loop over set
            if i-1 not in sorted_set: #if this value is first
                curr = i #initialize new current value
                count = 1 # itnialize temp count

                while curr+1 in sorted_set: #see if there is a seq and count it
                    curr += 1 #increment because its a sequence by 1
                    count += 1
                
                best_count = max(best_count,count) # end of seq or set, it will find max
            #then loops since the next value in the initial for loop set is probobly account for,
            #it will skip cause it counted the full sequence

        return best_count