class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        temp = arr
        final = []
        for i in range(len(arr)):
            if len(temp)>1:
                c = max(temp[0:-1])
                m = temp.index(c)
                if temp[-1]>c:
                    temp.pop()
                else:
                    temp = temp[m::-1]+temp[m+1: ]
                    final.append(m+1)
                    temp.reverse()
                    final.append(len(temp))
                    temp.pop()
        return final
                        
                
                
            
