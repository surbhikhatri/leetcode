class Solution:
    def maxScore(self, s: str) -> int:
        # num of 0's in left and 1's in right
        # total 1's 4 0, 1 + 4, 1 + 
        ones = sum([1 for c in s if c == "1"])
        zeros = 0
        res = 0
        for c in s[:-1]:
            if c == "1":
                ones -= 1
                res = max(res, zeros + ones)
            else:
                zeros += 1
                res = max(res, zeros + ones)
        return res




        