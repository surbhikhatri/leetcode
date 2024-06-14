class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:  
        maxdiag = 0
        maxarea = 0
        for dim in dimensions:
            l, w = dim[0], dim[1]
            diag = sqrt(l * l + w * w)
            if diag > maxdiag:
                maxdiag = diag
                maxarea = l * w
            elif diag == maxdiag:
                maxarea = max(maxarea, l * w)
        return maxarea        