class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if x[0: ] == x[: : -1]:
            return 1
        else:
            return 0 
