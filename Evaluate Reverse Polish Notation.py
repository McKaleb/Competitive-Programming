class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+","/","*","-"]
        j = 0
        for i in range(len(tokens)):
            if tokens[i] in operands:
                if tokens[i] == "+":
                    stack.append(int(stack[j-2])+int(stack[j-1]))
                elif tokens[i] == "-":
                    stack.append(int(stack[j-2])-int(stack[j-1]))
                elif tokens[i] == "*":
                    stack.append(int(stack[j-2]) * int(stack[j-1]))
                else:
                    stack.append(int(int(stack[j-2])/int(stack[j-1])))
                stack.pop(-2)
                stack.pop(-2)
                j-=1
            else:
                stack.append(tokens[i])
                j+=1
        return stack[0]
