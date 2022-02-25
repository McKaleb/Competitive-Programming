import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return 1
        if n < 3:
            return 0
        
        val = n
        while val == int(val):
            if val == 1 or val == 3:
                return 1
            val/=9
        else:
            return 0
