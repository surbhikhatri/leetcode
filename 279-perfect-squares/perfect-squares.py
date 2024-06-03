class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0 
        for i in range(1, n + 1):
            tmpmin = float("inf")
            j = 1
            while j * j <= i:
                # add 1 for considering current element
                tmpmin = min(tmpmin, dp[i - j * j] + 1)
                j += 1
            dp[i] = tmpmin
        
        return dp[-1]
