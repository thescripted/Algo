class Solution:
    def check_permutation(self, s: str, t: str):
        if len(s) != len(t): 
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return False
        return True