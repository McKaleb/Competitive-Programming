class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            ones = bin(i)
            arr.append(ones.count('1'))
        return arr