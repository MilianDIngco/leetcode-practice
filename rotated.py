from typing import List
import random

'''
Think about the array as two split parts, left and right. 
Left will always be greater than right because its being rotated to the right
The biggest numbers will be rotated to the start of the array
The middle is in the left portion if middle is greater than the right
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r, curr_min = 0, len(nums) - 1, float("inf")
        
        while l < r:
            m = l + ((r - l) // 2) 
            curr_min = min(curr_min, nums[m])
            
            print("L: {} M: {} R: {}".format(l, m, r))
            print("L: {} M: {} R: {}".format(nums[l], nums[m], nums[r]))
            print("____________________")
            
            if nums[r] < nums[m]: 
                l = m + 1
            else:
                r = m - 1
        return min(curr_min, nums[l])
    
fail = 0
succ = 0    
    
for _ in range(200):
    a = Solution()
    nums = [random.randint(1, 20) for _ in range(100)]
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    ans = nums[0]
    rotate = random.randint(1, len(nums) - 1)
    nums = nums[-rotate:] + nums[:-rotate]
    print("Rotated by: {} Min: {}\nArray: {}".format(rotate, ans, nums))
    print("Res: {}".format(a.findMin(nums) == ans))
    if a.findMin(nums) == ans:
        succ += 1
    else:
        fail += 1

print(fail)
print(succ)