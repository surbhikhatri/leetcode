class Solution:
    def jobScheduling(self, st: List[int], et: List[int], p: List[int]) -> int:
        jobs = sorted(zip(st, et, p))

        cache = {}

        def dfs(i):
            if i == len(st):
                return 0
            
            if i in cache:
                return cache[i]

            # not includding the job
            res = dfs(i + 1)

            # including the job
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            cache[i] = res = max(res, dfs(j) + jobs[i][2])
            return res
        
        return dfs(0)