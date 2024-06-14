class Solution:
    def minOperations(self, s: str) -> int:
        count = 0
        # for even we expect 0. for odd we expect 1
        for i in range(len(s)):
            if i % 2 == 1: # odd
                count += 1 if s[i] == "0" else 0
            else:
                count += 1 if s[i] == "1" else 0





        return min(count, len(s) - count)

        