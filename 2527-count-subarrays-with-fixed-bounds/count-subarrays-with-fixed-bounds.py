class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # minpos, maxpos -> most recent positions of minK and maxk
        # left bound -> most recent position outside the mink, maxk range
        ans = 0
        minpos, maxpos, leftbound = -1, -1, -1
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                leftbound = i
            
            if num == minK:
                minpos = i
            
            if num == maxK:
                maxpos = i
            
            ans += max(0, min(minpos, maxpos) - leftbound)
        
        return ans
