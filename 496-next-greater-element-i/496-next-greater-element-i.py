class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = {}
        stack = [nums2[0]]
        for i in range(1,len(nums2)):
            while stack and nums2[i]>stack[-1]:
                mapper[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for i in stack:
            mapper[i]=-1
        return [mapper[key] for key in nums1]
