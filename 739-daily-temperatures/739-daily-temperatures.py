class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        new = []
        stack = []
        for idx,i in enumerate(temperatures):
            while stack and i>stack[-1][-1]:
                y = idx-stack[-1][0]
                new.append([stack.pop(),y])
            stack.append([idx,i])
        for i in stack:
            new.append([i,0])
        new.sort()
        return [i[1] for i in new]
        
         
