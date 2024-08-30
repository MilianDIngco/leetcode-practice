from typing import List
import random

def swap(arr: List[int], one: int, two: int):
    print("1: {} 2: {}".format(one, two))
    temp = arr[two]
    arr[two] = arr[one]
    arr[one] = temp

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        ans = 0
        
        #sort by positions
        sorted_pos = sorted(list(enumerate(position)), key=lambda x: x[1])
        sorted_pos.reverse()
        for i, j in sorted_pos:
            eta = (target - position[i]) / speed[i]
            while len(stack) > 0 and eta > stack[-1]:
                stack.pop()
            if len(stack) == 0:
                ans += 1
            stack.append(eta)
            print(eta)
        return ans

a = Solution()
target=10
position=[0,4,2]
speed=[2,1,3]
print(a.carFleet(target, position, speed))
