class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict_list = {}
        for i in nums:
            if i in dict_list:
                dict_list[i] += 1
            else:
                dict_list[i] = 1
        key_list = list(dict_list.keys())
        value_list = list(dict_list.values())
        position = value_list.index(min(dict_list.values()))
        return key_list[position]