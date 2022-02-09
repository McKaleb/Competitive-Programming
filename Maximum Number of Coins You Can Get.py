class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        m = len(piles)
        count = 0
        for i in range(m//3, m, 2):
            count += piles[i]
        return count
