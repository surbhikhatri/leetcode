class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        l, r = [0] * n, [0] * n
        for i in range(1, n):
            l[i] = max(h[i - 1], l[i - 1])
        
        for i in range(n - 2, -1, -1):
            r[i] = max(h[i + 1], r[i + 1])
    
        res = 0
        for i in range(n):
            res += max(0, min(l[i], r[i]) - h[i])
        return res




        