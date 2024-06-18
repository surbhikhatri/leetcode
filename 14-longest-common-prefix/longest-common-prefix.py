class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = min([len(s) for s in strs])

        res = ""
        for i in range(minlen):
            fnd = True
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    fnd = False
            
            if fnd == True:
                res += strs[0][i]
            else:
                break
        
        return res

        