class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(char for char in s if char.isalnum()).lower()
        if cleaned != cleaned[::-1]:
            return False
        return True