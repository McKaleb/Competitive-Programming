import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return 1
        val = n
        while val == int(val) and n>=3:
            if val == 1 or val == 3:
                return 1
            val/=9
        else:
            return 0
