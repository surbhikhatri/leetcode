class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # sequential digits, each digit in a num is one more than prev
        # sorted list in low to high inclusive
        res = []

        def dfs(digit, cur):
            if cur < low: # keep continuing
                if digit < 9:
                    dfs(digit + 1, (cur * 10) + (digit + 1))

            elif cur >= low and cur <= high: # add to result and continue
                res.append(cur)
                if digit < 9:
                    dfs(digit + 1, (cur * 10) + (digit + 1))

            if cur > high: # return 
                return 


        for i in range(1, 9):
            dfs(i, i)

        res.sort()
        return res













        result = []

        for i in range(1, 10):
            num = i

            for j in range(i + 1, 10):
                num = num * 10 + j

                if low <= num <= high:
                    result.append(num)

        return sorted(result)


        
        res = []
        sd, ed = int(str(low)[0]), int(str(high)[0])
        csize = len(str(low))
        esize = len(str(high))

        while csize <= esize:
            for i in range(sd, 9):
                cur = [str(j) for j in range(i, min(10, i + csize))]
                cur = "".join(cur)
                if int(cur) <= high and int(cur) >= low and int(cur) not in res:
                    res.append(int(cur))
                elif int(cur) > high:
                    break
            csize += 1
            sd = 1
        
        return res
