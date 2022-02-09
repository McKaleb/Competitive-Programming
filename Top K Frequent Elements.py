class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = Counter(nums)
        sort = sorted(Dict.items(), key=lambda x: x[1], reverse=True)
        print(sort)
        new = []
        for i in range(k):
            new.append(sort[i][0])
        return new
