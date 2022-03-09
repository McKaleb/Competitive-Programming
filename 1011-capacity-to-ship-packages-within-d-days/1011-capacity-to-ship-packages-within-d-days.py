class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        x = max(weights)
        y = sum(weights)
        left = x
        right = y
        
        best = left
        while left<=right:
            mid=left + (right-left)//2
            dayscap = [0]*days
            i = 0
            j = 0
            while j < len(weights) and i < len(dayscap):
                if dayscap[i]+weights[j]<=mid:
                    dayscap[i]+=weights[j]
                    j+=1
                else:
                    i+=1
            if dayscap[-1]==0 or sum(dayscap) == y:
                best = mid
                right = mid-1
            else:
                left = mid+1
        return best
                                