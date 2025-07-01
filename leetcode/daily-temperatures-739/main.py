class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and stack[-1][1] <= temperatures[i]:
                stack.pop()
            
            if stack:
                pos, _ = stack[-1]
                res[i] = abs(i - pos)
            stack.append((i, temperatures[i]))

        
        return res



