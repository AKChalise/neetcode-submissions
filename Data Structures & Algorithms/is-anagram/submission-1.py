class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        # Sort the strings and compare
        return sorted(s) == sorted(t)

