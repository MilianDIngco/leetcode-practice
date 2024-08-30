import random
from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    ans = [] 
    nums.sort() # this is so we can approach the array from both ends using two pointer
    
    for i, a in enumerate(nums): #used enumerate because the current value of i (a) is the target
        if a > 0: #since we're only checking elements to the right of i, if nums at i is > zero then all elements to the right are positive thus can never sum to zero
            break
        
        if i > 0 and a == nums[i - 1]: #skips elements where i is a duplicate but all possible combinations of that element have already been found
            continue
    
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                ans.append([a, nums[l], nums[r]])
                l += 1 # don't want to check the same elements anymore
                r -= 1 # increment both bc the only way r is used again is if l is the same element again therefore the combination is the same
                while nums[l] == nums[l - 1] and l < r: #ensures even if r is a duplicate element, l isn't and r will be changed again
                    l += 1    
    
    return ans

nums = [round(random.random() * 20) - 10 for _ in range(20)]
nums = [-2,0,0,2,2]
print(nums)
ans = threeSum(nums)
print("----final----")
print(ans)
print(len(ans))

'''
#sort the array
    nums.sort();
    ans = []
    print(nums)
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i != 0 and nums[i] == nums[i - 1]:
            continue
        a = i + 1
        b = len(nums) - 1
        target = -nums[i]
        while(a < b):
            print("A: {} B: {} I: {}".format(a, b, i))
            while nums[a] + nums[b] < target or (nums[a] == nums[a + 1] and a < b):
                a += 1
            while nums[a] + nums[b] > target or (nums[b] == nums[b - 1] and a < b):
                b -= 1
            if a >= b:
                break
            if nums[a] + nums[b] == target:
                curr = [nums[i], nums[a], nums[b]]
                ans.append(curr)
                print("----added----")
                print(curr)
                a += 1
                b -= 1
                while nums[i] == nums[i + 1] and a < b:
                    i += 1
        
    return ans
'''
    
'''
#sort the array
nums.sort()
ans = []
print(nums)

i = 0
while(len(nums) >= 3 and i < len(nums) - 1):
    #select the first element to be the target
    target = -nums[i]
    a = 0
    b = len(nums) - 1
    while(a < b):
        if(a == i):
            a += 1
        if(b == i):
            b -= 1

        print("A: {} B: {} target: {}".format(nums[a], nums[b], target))
        if(nums[a] + nums[b] < target): 
            a += 1
        elif(nums[a] + nums[b] > target):
            b -= 1
        elif(nums[a] + nums[b] == target):
            curr = [nums[i], nums[a], nums[b]]
            exists = False
            for answer in ans:
                if(set(answer) == set(curr)):
                    exists = True
                    break
            if not exists:
                ans.append(curr)
            break
    i += 1
return ans
'''

'''
def threeSum(nums: List[int]) -> List[List[int]]:
    #sort the array
    nums.sort()
    ans = []
    print(nums)
    
    i = 0
    while(len(nums) >= 3):
        #select the first element to be the target
        target = -nums[i]
        a = 1
        b = len(nums) - 1
        while(a < b):
            print("A: {} B: {} target: {}".format(nums[a], nums[b], target))
            if(nums[a] + nums[b] < target): 
                a += 1
            elif(nums[a] + nums[b] > target):
                b -= 1
            elif(nums[a] + nums[b] == target):
                curr = [nums[0], nums[a], nums[b]]
                nums.pop(b)
                nums.pop(a)
                ans.append(curr)
                break
        nums.pop(0)
    return ans
'''


