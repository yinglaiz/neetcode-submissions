class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s,reverse=True) == sorted(t,reverse=True)

        