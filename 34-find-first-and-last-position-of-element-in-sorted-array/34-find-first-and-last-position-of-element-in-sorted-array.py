class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        start = 0
        low = 0
        high = len(nums)-1
        end = 0
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]>=target:
                if nums[mid]==target:
                    start = mid
                right = mid-1
            else:
                left = mid+1
        while low <= high:
            mid2 = low + (high-low)//2
            if nums[mid2]<=target:
                if nums[mid2]==target:
                    end = mid2
                low = mid2+1
            else:
                high = mid2-1
        if not nums:
            return [-1,-1]
        elif nums[start] == target and nums[end]==target:
            return [start,end]
        else:
            return [-1,-1]
            
