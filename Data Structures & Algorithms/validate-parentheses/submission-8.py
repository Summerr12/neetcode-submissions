class Solution:
    def isValid(self, s: str) -> bool:

        #if open bracket, open, then continue till closing
        #if open, close, then check if they pair
        #stack only open brackets
        if len(s) % 2 != 0: return False

        stack = []
        di = { 
            "[": "]", 
            "(": ")", 
            "{": "}", 
        }

        for i in s:
            if i in di:
                stack.append(i)
            else:
                #check if there is no stack and just closing
                if len(stack) == 0 or di[stack.pop()] != i: 
                    return False


        if len(stack)>0: return False
        return True
            