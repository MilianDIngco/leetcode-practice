from typing import List

'''
its like rolling up a rubber band along the sides of a container
|   #   #   #|
| # #   ## ##|
| # ## ######|
|############|

if the shape is like a mountain, itll catch all the little dips and count up until the height of the rubber band
if the shape is like a U, then the topography of the inside doesn't matter since it will all fill up until the lips

'''

def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    sum_area = 0
    max_l, max_r = height[l], height[r]
    while l < r: 
        if max_l < max_r:
            l += 1
            max_l = max(max_l, height[l])
            sum_area += max_l - height[l]
        else:
            r -= 1
            max_r = max(max_r, height[r])
            sum_area += max_r - height[r]
                    
    return sum_area

def print_img(height: List[int]):
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
                
height = [0,2,0,3,1,0,1,3,2,1, 2, 3]
print_img(height)
print(trap(height))

'''
l, r = 0, 1
sum_area = 0
    
while l < len(height) - 2:
        while height[l] < 1 or height[l + 1] >= height[l]: #1
            l += 1
            r = l + 1
        
        max_height = 0x
        while max_height < height[l] and r < len(height) - 1: #2
            max_height = r if height[r] > height[max_height] else max_height
            r += 1
        r = max_height

        for i in range(l + 1, max_height): #3
            sum_area += min(height[l], height[max_height]) - height[i]
            print(sum_area)
        l = r
        r = l + 1
return sum_area
'''

'''
    l, r = 0, 1
    sum_area = 0
    # need to find a left and right wall
    while r < len(height) - 1:
        while height[l] < 1 or height[l + 1] >= height[l]: #find a valid left wall 
            print("L: {}".format(l))
            l += 1
            r = l + 1
        
        max_height = height[r]
        while max_height < height[l] and r < len(height) - 1: #go to the end of the list and find the next tallest wall
            print("R: {} Max: {}".format(r, max_height))
            max_height = r if height[r] > height[max_height] else max_height
            r += 1
        r = max_height
        
        # THEORETICALLY max_height should have the index of the right wall
        #now i should be able to just sum the areas between the wall
        print("Left wall: {} Right wall: {}".format(l, r))
        
        for i in range(l + 1, max_height):
            sum_area += min(height[l], height[max_height]) - height[i]
        print("Sum area: {}".format(sum_area))
        l = r
        r = l + 1
        
        
    return sum_area
    '''