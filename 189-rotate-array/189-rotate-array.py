class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rot = 0
        for i in range(k):
            rot = nums[-1]
            nums.pop()
            nums.insert(0, rot)
            
        