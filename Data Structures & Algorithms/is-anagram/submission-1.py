class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []
        for n in s:
            list_s.append(n)

        for n in t:
            list_t.append(n)

        list_s.sort()
        list_t.sort()
        if list_s == list_t:
            return True;
        return False