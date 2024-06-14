class Solution:
    def toHex(self, num: int) -> str:
        # hexadecimal = base 16, 4 digits
        dmap = "0123456789abcdef"
        if num < 0:
            num = (1 << 32) + num
        res = ""
        if num == 0:
            return "0"
        while num > 0:
            rem = num % 16
            res += dmap[rem]
            num //= 16
        return res[::-1]

        