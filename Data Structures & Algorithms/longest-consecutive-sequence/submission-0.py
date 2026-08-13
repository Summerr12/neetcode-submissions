class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        uniq_nums = sorted(set(nums))
        curr_stk = 1
        max_stk = 1

        for i in range(1, len(uniq_nums) ):
            print(uniq_nums[i])
            if uniq_nums[i-1]+1 == uniq_nums[i]:
                curr_stk += 1
            else:
                max_stk = max(max_stk, curr_stk)
                curr_stk = 1
        return max(max_stk, curr_stk)