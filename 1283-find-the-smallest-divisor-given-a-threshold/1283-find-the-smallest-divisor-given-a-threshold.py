import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = 0
        while left<=right:
            mid=left + (right-left)//2
            x = 0
            istrue = True
            for num in nums:
                x += math.ceil(num/mid)
                if x > threshold:
                    istrue = False
                    break
                    
            if x <= threshold and istrue:
                ans = mid
                right = mid-1
            else:
                left = mid+1
        # y = sum(nums)
        # if y <= threshold and 1 < ans:
        #     return 1
        # else:
        return ans