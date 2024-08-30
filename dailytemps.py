from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair [index, value]
        ans = [0] * len(temperatures)
        
        for i, j in enumerate(temperatures):
            while len(stack) > 0 and j > stack[-1][1]:
                index = stack.pop()[0]
                ans[index] = i - index
            stack.append([i, j])
        
        return ans
    
a = Solution()
temps = [30,38,30,36,35,40,28]
print(a.dailyTemperatures(temps))

# [1,4,1,2,1,0,0]