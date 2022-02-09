class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        j = -1
        Max = nums[0]+nums[-1]
        for i in range(len(nums)//2):
            if nums[i] + nums[j]> Max:
                Max = nums[i] + nums[j]
            j-=1
        return Max
