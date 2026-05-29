class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True

        for j in range(n):
            if p[j] == '*':
                dp[j + 1] = dp[j]

        for i in range(m):
            new = [False] * (n + 1)
            for j in range(n):
                if p[j] == '*':
                    new[j + 1] = new[j] or dp[j + 1]
                elif p[j] == '?' or s[i] == p[j]:
                    new[j + 1] = dp[j]
            dp = new

        return dp[n]