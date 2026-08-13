class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False

        #if open bracket, open, then continue till closing
        #if open, close, then check if they pair
        #stack only open brackets
        #
        #
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
                if len(stack) == 0: return False
                popped_open = stack.pop()
                if di[popped_open] != i:
                    return False

        if len(stack)>0: return False
        return True
            