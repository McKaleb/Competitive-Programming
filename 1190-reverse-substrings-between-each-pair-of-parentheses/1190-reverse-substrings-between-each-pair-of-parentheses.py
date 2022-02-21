class Solution:
    def reverseParentheses(self, s: str) -> str:
        t = list(s)
        c=t.count("(")
        x = 0
        while x < c: 
            j = 0
            i = 0
            while i < len(t):
                if t[i] == "(":
                    j = i
                elif t[i]==")":
                    t=t[:j]+t[j+1:i][::-1]+t[i+1:]
                    print(t)
                    x+=1
                    break
                i+=1
        return "".join(t)