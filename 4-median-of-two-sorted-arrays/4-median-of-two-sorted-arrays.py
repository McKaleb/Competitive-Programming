class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = nums1+nums2
        print(num)
        c = len(num)
        d = int(c/2)
        num.sort()
        return num[int(c/2)] if c%2!=0 else (num[d-1]+num[d])/2