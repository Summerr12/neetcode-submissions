class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        clean=""
        for i in s:
            if i.isalnum():
                clean+= i
        print("".join(reversed(clean.lower())) , clean)
        if "".join(reversed(clean)) == clean :
            return True
        return False
        