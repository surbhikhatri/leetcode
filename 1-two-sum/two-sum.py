class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [ h[target - nums[i]], i ]
            else:
                h[nums[i]] = i
        return 
        