class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        j = 0
        for row in grid:
            left = 0
            right = len(row)-1
            start = 0
            while left <= right:
                mid = left+(right-left)//2
                
                if row[mid] < 0:
                    right = mid-1
                    start = mid
                else:
                    left = mid+1
            if row[start] < 0:
                j += len(row[start:])
        return j