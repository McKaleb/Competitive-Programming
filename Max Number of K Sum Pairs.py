class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        Dict = Counter(nums)
        Nums = list(Dict.keys())
        i = 0
        while i < len(Nums):
            if Nums[i]*2==k and Dict[Nums[i]]>=2:
                Dict[Nums[i]]-=2
                count+=1
            elif Nums[i]<k and Dict[Nums[i]]>0 and (k-Nums[i]) in Dict and Dict[k-Nums[i]]>0:
                if Nums[i]==k-Nums[i] and Dict[Nums[i]] <= 1:
                    i+=1
                else:
                    Dict[Nums[i]]-=1
                    Dict[k-Nums[i]]-=1
                    count+=1
            else:
                i+=1
        return count
