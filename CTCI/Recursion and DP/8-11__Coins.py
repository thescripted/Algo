class Solution:

    def coins(self, n: int) -> int:
        coinSet = set()
        initSol = reduceValue(n)
        self._coins(initSol, coinSet)
    
    def _coins(self, init, set):
        for i in init:
            if i == 1:
                continue

    
    def reduceValue(self, n):
        sol = []
        while (n > 0):
            if (n // 25 > 0):
                n = n - 25
                sol.append(25)
                continue
            if (n // 10 > 0):
                n = n - 10
                sol.append(10)
                continue
            if (n // 5 > 0):
                n = n - 5
                sol.append(5)
                continue
            n = n - 1
            sol.append(1)
        return sol

s = Solution()

print(s.reduceValue(25))