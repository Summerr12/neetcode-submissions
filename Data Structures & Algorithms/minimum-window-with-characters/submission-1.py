class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # dict insert all chars that are in T, ignore the rest
        # as keys, insert the index in a array
        # {
        # x: 3. 5. 11
        # y: 1. 8. 12
        # z: 9. 24
        # }

        # highest val is z at 24 
        # shortest val is x at 3
        # y is in range at 8 and 12

        # return s[index of x: index of z]

        if len(s) < len(t): return ""

        need = {}
        for c in t:
            need[c] = need.get(c,0) +1
        needCount = len(need) #length of distinct vals

        window = {}
        have = 0 # distinct value count
        left = 0
        result = [-1,-1]
        resultLen = float("inf")

        for right in range(len(s)): #loop through whole s
            c = s[right]
            if c in need: #if character matters
                window[c] = window.get(c,0) + 1
                if window[c] == need[c]: #check if we have met one of need's requirements
                    have += 1

            while have == needCount: #window loop when finding all pieces
                if (right-left+1) < resultLen:
                    result = [left,right]
                    resultLen = right-left+1

                if s[left] in need:    
                    window[s[left]] -= 1 #auto shrink to find the next window
                    if window[s[left]] < need[s[left]]:
                        #if the removed char is needed and there is less of the char than required, 
                        #we say we dont have that distinct val anymore
                        have -= 1
                left += 1 #shrink the actual window range
        left, right = result
        return s[left:right+1] if resultLen != float("inf") else ""


        


        return ""