class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        y = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                del nums[i]
                y+=1
            else:
                i+=1
        for i in range(y):
            nums.append(0)