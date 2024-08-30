from typing import List

'''
THING TO NOTICE FOR HISTOGRAM HARD
Extend the index to the left
for example
  #
 ##
####
   ^
   index of this column should be 0 since the area considered extends to the 0th index
'''

class Solution:
    def print_img(self, height: List[int]):
        max_height = max(height)
        for row in range(max_height):
            print("|", end="")
            for col in height:
                if col >= max_height - row:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("|")
        print("|", end="")
        for i in range(len(height)):
            print("{}".format(i), end="")
        print("|")
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: [index, value]
        max_area = 0
        heights.append(0)
        
        for i, j in enumerate(heights):
            last_index = -1
            while len(stack) > 0 and j < stack[-1][1]:
                col = stack.pop()
                area = col[1] * (i - col[0])
                max_area = area if area > max_area else max_area
                last_index = col[0]
            if last_index != -1:
                stack.append([last_index, j])
            else:
                stack.append([i, j])
            # print("Stack: {} Max_area: {}".format(stack, max_area))
            
        return max_area
    
heights = [1,3,7]
a = Solution()
a.print_img(heights)
print("Answer: {}".format(a.largestRectangleArea(heights)))
