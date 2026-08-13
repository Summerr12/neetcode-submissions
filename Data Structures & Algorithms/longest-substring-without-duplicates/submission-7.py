class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        conditions
        check if value is a letter using .isalnum
        check if value is already used in substring
        iterate a window, 
        if c is new, include in string
        else, count max length and cut based off old c

        """
        if len(s) ==0: return 0
        if len(s) ==1: return 1

        subr=""
        best_len=0
        for i in s:
            if i not in subr:
                subr += str(i)
            else:
                best_len = max(best_len,len(subr))

                index = subr.find(i)
                subr = subr[index+1:]+i
        
        return max(best_len,len(subr))
