class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n <= 2:
            return dp[n-1]
        
        m = 3
        while m <= n:
            dp.append(dp[(m - 1) - 1] + dp[(m - 2) - 1])
            m += 1 
        return dp[-1]