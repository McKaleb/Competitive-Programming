class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s)%2==1:
            return False
        opening=0
        closing=0
        free=0
        for i in range(0,len(s)):
            if locked[i]=="0":
                free+=1
            else:
                if s[i]=="(":
                    opening+=1
                else:
                    closing+=1
            if closing>opening+free:
                return False
        opening=0
        closing=0
        free=0
        for i in range(len(s)-1,-1,-1):
            if locked[i]=="0":
                free+=1
            else:
                if s[i]=="(":
                    opening+=1
                else:
                    closing+=1
            if opening>closing+free:
                return False

        return True