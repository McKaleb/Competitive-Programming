class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        for i in nums1:
            for j in nums2[nums2.index(i)+1:]:
                if j>i:
                    lst.append(j)
                    break
            else:
                lst.append(-1)
        return lst