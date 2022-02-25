class Solution:
    def hIndex(self, citations: List[int]) -> int:
        x = len(citations)
        hindex = 0 
        if citations[0]>=x:
            return x
        left = 0
        right = x-1
        end,key = 0,0
        istrue = True
        while left <= right:
            
            mid = left + (right-left)//2
            leng = len(citations[mid:])
            if leng >= citations[mid]:
                hindex = citations[mid]
                try:
                    end = citations[mid+1]
                    key = mid+1
                except IndexError:
                    istrue = False
                left = mid+1
            else:
                right=mid-1
        ans = hindex
        z = leng = len(citations[key:])
        if citations[key-1] != citations[key] and istrue:
            while hindex <= end:
                mid = hindex+(end-hindex)//2
                if mid <= z:
                    ans = mid
                    hindex = mid+1
                else:
                    end = mid-1
        return ans
        print(hindex,end,z)