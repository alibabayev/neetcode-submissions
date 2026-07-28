class Solution:
    # Backtracking
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def dfs(i):
            if i >= n:
                res.append(part[:])
                return
            
            for j in range(i, n):
                if dp[i][j]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res    