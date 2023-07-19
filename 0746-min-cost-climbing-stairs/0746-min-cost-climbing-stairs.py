class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        m = 3
        dp = cost[:2]  # dp[i]: min overall cost depart from step i
        while m <= len(cost):
            dp.append(min(dp[(m - 2) - 1] + cost[m - 1], 
                          + dp[(m - 1) - 1] + cost[m - 1]))
            m += 1
        return min(dp[-2], dp[-1])