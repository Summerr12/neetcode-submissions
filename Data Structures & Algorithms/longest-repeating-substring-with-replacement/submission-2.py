class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what if i didnt care about the values and used the window of K
        # we can find what to best replace in K
        # ABBBCB
        # k=2
        # based off unique dict we can keep in check the values 
        # a 1
        # a 1 b 1
        # a 1 b 2
        # a 1 b 3
        # a 1 b 3 c 1
        # stop and frame len IF 
        #     there are k+1 more unique chars 
        #     or any of the dict's smallest counts other than the greatest count is = k
        # then shrink 

        if len(s)==1: return 1

        countedChars = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            #incrementing
            if s[right] in countedChars:
                countedChars[s[right]] += 1 
            else:
                countedChars[s[right]] = 1
            #keeps track of highest freq char
            max_freq = max(max_freq, countedChars[s[right]])

            #finds window to check if there is enough k replacements to continue the streak after every increment
            window_len = right-left+1
            if window_len - max_freq >k: #if not enough replacemen†s, shrink window and remove from dict
                countedChars[s[left]] -= 1
                left += 1

            max_length = max(max_length, right-left+1)
        
        return max_length