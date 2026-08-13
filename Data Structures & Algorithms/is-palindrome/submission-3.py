class Solution:
    def isPalindrome(self, s: str) -> bool:
        prep = s.lower()
        cleaned = ''.join(char for char in prep if char.isalnum())
        # print(cleaned)
        rev_clean = cleaned[::-1]
        # print(cleaned, rev_clean)
        for i in range(len(cleaned)):
            if cleaned[i] != rev_clean[i]:
                return False
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s = s.lower().strip()
        # clean=""
        # for i in s:
        #     if i.isalnum():
        #         clean+= i
        # print("".join(reversed(clean.lower())) , clean)
        # if "".join(reversed(clean)) == clean :
        #     return True
        # return False
        