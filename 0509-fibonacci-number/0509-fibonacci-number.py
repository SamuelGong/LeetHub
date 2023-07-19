class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n <= 1:
            return dp[n]
        
        m = 2
        while m <= n:
            dp.append(dp[m - 1] + dp[m - 2])
            m += 1
        return dp[-1]