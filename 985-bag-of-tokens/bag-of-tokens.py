class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        res = 0
        score = 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if tokens[l] <= power: # face up
                power -= tokens[l]
                score += 1
                l += 1
                res = max(res, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        
        return res


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        tokens.sort()
        n = len(tokens)
        score = 0
        max_score = 0
        left = 0
        right = n - 1
        
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
                
        return max_score