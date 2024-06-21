class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # dp to store state: (dice remaining, cur sum)
        # n dice -> k faces from 1 to k, target, return # of possible ways out of k**n 
        # % 10 ** 9 + 7
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
        
        return count(n, target)     
            



