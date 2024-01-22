class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        s = sorted(s)
        t = sorted(t)

        for i, j in zip(s, t):
            if i.lower() != j.lower():
                return False

        return True