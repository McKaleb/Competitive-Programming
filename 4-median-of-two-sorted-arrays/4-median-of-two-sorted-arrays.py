class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        c = len(num)
        d = int(c/2)
        num.sort()
        return num[d] if c%2!=0 else (num[d-1]+num[d])/2