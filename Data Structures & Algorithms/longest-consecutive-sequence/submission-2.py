class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums: return 0

        #if ther eis only one num, return num
        #if there is more than one num, check the sequence
        #create a set of sorted values
        if len(nums) == 0: return 0

        sorted_set = sorted(set(nums))
        print(sorted_set)

        count = 1
        best_count = 1

        for i in sorted_set:
            if i-1 not in sorted_set: #if it is the first num
                curr = i
                count = 1

                while curr+1 in sorted_set:
                    curr += 1
                    count += 1
                
                best_count = max(best_count,count)

        return best_count