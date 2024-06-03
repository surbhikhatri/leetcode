class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        dp = {}
        def dfs(i, remain):
            if remain <= 0:
                # painted all walls, will cost 0 to paint the remaining walls
                return 0
            
            if i == len(cost):
                # did not find a solution 
                return float("inf")
            
            if (i, remain) in dp:
                return dp[(i, remain)]

            # paint the wall
            paint = cost[i] + dfs(i + 1, remain - 1 - time[i])

            # skip the wall
            skip = dfs(i + 1, remain)
            dp[(i, remain)] = min(skip, paint)

            # return min
            return dp[(i, remain)]


        return dfs(0, len(cost))