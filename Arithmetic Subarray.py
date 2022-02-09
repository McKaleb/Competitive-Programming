class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        final = []
        for i in range(len(l)):
            Dict = {}
            j = l[i]
            Nums = sorted(nums[l[i]:r[i]+1])
            for j in range(len(Nums)-1):
                if Nums[j+1] - Nums[j] not in Dict:
                    Dict[Nums[j+1] - Nums[j]] = 1
                else:
                    Dict[Nums[j+1] - Nums[j]] += 1
            m = list(Dict.keys())
            if len(m) == 1:
                final.append(1)
            else:
                final.append(0)
            print(m)
        return final
