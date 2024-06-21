class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp to store state: (dice remaining, cur sum)
        # n dice -> k faces from 1 to k, target, return # of possible ways out of k**n 
        dp = [0] * (target + 1) # number of ways to roll i
        dp[0] = 1
        mod = 10 ** 9 + 7
        for dice in range(n): # num of dice
            next_dp = [0] * (target + 1)

            for val in range(1, k + 1): # k faces
                for total in range(val, target + 1): # look at all the values in dp array
                    # total = 8 ==  ways to roll 3 + ways to roll 5
                    next_dp[total] = (next_dp[total] + dp[total - val]) % mod
            
            dp = next_dp
        
        return dp[target]






        mod = 10 ** 9 + 7
        cache = {}
        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0

            if (n, target) in cache:
                return cache[(n, target)]

            res = 0
            for val in range(1, k + 1):
                res = (res + count(n - 1, target - val)) % mod
            
            cache[(n, target)] = res
            return res
        
        return count(n, target)  # top down    
            



