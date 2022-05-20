class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        num = nums[0]
        lst = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]==num:
                count += 1
            else:
                lst.append(nums[i])
                num = nums[i]
        nums.clear()
        for i in lst:
            nums.append(i)
            