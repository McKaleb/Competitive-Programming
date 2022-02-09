class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        Dict = Counter(arr)
        sort_orders = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
        tot = 0
        count = 0
        for i in sort_orders:
            if tot < len(arr)//2:
                count+=1
                tot+=i[1]
            else:
                break
        return count
