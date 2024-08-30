from typing import List
import random

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m = 0, len(nums) - 1, 0
        print(nums)
        
        while l <= r:
            m = l + ((r - l) // 2)
            
            print("L: {} M: {} R: {}".format(l, m, r))

            if target >= nums[l] and nums[m] < nums[l]:
                r = m - 1
            elif target <= nums[r] and nums[m] > nums[r]:
                l = m + 1
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1 
            else: 
                target == nums[m]
                return m

        return m


fail = 0
succ = 0    

for _ in range(200):
    a = Solution()
    nums = [random.randint(1, 10) for _ in range(100)]
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    rotate = random.randint(1, len(nums) - 1)
    nums = nums[-rotate:] + nums[:-rotate]
    ans = random.randint(0, len(nums) - 1)
    #print("Rotated by: {} Index: {}\nArray: {}".format(rotate, ans, nums))

    res = a.search(nums, nums[ans])
    print("Res: {} ans: {}".format(res == ans, ans))
    print("---------------------------------")
    if res == ans:
        succ += 1
    else:
        fail += 1

print(fail)
print(succ)
