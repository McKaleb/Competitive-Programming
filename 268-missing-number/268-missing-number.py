class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = nums + list(range(len(nums)+1))
        print(nums)
        theNum = 0
        for num in nums:
            theNum ^= num
        return theNum
            