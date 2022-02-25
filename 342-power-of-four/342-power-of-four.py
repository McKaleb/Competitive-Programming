class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return 1
        val = n
        while val == int(val) and n>=4:
            if val == 1 or val == 4:
                return 1
            val/=16
        else:
            return 0  