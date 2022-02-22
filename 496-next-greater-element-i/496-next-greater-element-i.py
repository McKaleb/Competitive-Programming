class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lst = []
        y = len(nums2)
        for i in nums1:
            for j in nums2[nums2.index(i)+1:]:
                if j>i:
                    lst.append(j)
                    break
                # if j == nums2[-1]:
                #     lst.append(-1)
            else:
                lst.append(-1)
        return lst