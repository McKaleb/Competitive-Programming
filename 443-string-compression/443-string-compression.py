class Solution:
    def compress(self, chars: List[str]) -> int:
        newlist =[chars[0]]
        char = chars[0]
        count = 1
        for i in range(1,len(chars)):
            if chars[i]==char:
                count+=1
            else:
                if count>1:
                    for j in str(count):
                        newlist.append(j)
                count = 1
                newlist.append(chars[i])
                char = chars[i]
                
        if count>1:
            for i in str(count):
                newlist.append(i)
        print(newlist)
        chars.clear()
        for i in newlist:
            chars.append(i)
                
        