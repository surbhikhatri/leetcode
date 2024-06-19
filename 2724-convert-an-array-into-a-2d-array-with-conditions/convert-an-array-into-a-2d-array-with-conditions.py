class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # 1D to 2D array, distinct in each row, #rows minimum

        nums.sort()
        fmap = defaultdict(int)
        for n in nums:
            fmap[n] += 1
        r = max(fmap.values())
        res = [[] for _ in range(r)] # max duplicates, # of rows

        j = 0
        for k, v in fmap.items():
            for _ in range(v):
                if j == r:
                    j = 0
                res[j].append(k)
                j += 1
        
        return res