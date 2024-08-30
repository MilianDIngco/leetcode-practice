from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = (r - l) * min(height[l], height[r])
        print(area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        ans = max(area, ans)
        
    return ans

height = [1,1]
print(maxArea(height))