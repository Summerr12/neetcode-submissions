class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        rev_clean = cleaned[::-1]
        for i in range(len(cleaned)):
            if cleaned[i] != rev_clean[i]:
                return False
        return True