class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        for num in range(len(nums)+1):
            if num not in nums:
                return num
            