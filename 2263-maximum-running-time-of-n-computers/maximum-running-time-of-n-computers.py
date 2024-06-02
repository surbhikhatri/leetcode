class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        l, r = 1, sum(b) // n

        while l < r:
            t = r - (r - l) // 2
            e = 0

            for p in b:
                e += min(p, t)
            
            if e // n >= t:
                l = t
            else:
                r = t - 1
        
        return l

        