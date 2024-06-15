class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # move 4 directions, return num of 
        mod = 10 ** 9 + 7
        in_range = lambda x, y: 0 <= x < m and 0 <= y < n

        @cache
        def go(i, j , moves):
            if not in_range(i, j):
                return 1 # crossed the boundary, add 1 to res
            
            if moves == 0:
                return 0 # out of moves base case, return 0 because boundary not reached
            
            # temp result
            res = 0
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ti = i + di
                tj = j + dj
                res += go(ti, tj, moves - 1)
                res %= mod
            return res
        
        return go(startRow, startColumn, maxMove)
