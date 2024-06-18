class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # each child at most 1 cookie? greedy
        # child[i] has greed g[i] -> min size cookie a child wants
        # each cookie j has size of s[j, s[j] >= g[i] - assign j th cookie to ith child

        g.sort()
        s.sort()

        cur = 0
        res = 0
        for size in s:
            if cur < len(g) and size >= g[cur]:
                cur += 1
                res += 1
        
        return res


        