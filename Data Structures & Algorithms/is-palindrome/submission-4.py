class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        rev_clean = cleaned[::-1]
        # for i in range(len(cleaned)):
        if cleaned != rev_clean:
                return False
        return True