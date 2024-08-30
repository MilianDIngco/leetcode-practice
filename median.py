import random
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        one, two = nums1, nums2
        length = len(nums1) + len(nums2)
        half = length //2
        
        if len(two) < len(one):
            two, one = one, two
        
        l, r , m = 0, len(one) - 1, 0
        while True:
            m = (l + r) // 2
            m2 = half - m - 2; 
            
            oneL = one[m] if m >= 0 else float("-infinity")
            oneR = one[m + 1] if m + 1 < len(one) else float("infinity")
            twoL = two[m2] if m2 >= 0 else float("-infinity")
            twoR = two[m2 + 1] if m2 + 1 < len(two) else float("infinity")
            
            '''[oneL][oneR]'''
            '''[twoL][twoR]'''
            
            if oneL <= twoR and oneR >= twoL:
                if length % 2 == 0:
                    return (max(oneL, twoL) + min(oneR, twoR)) / 2
                return min(oneR, twoR)
            elif oneL > twoR:
                r = m - 1
            else:
                l = m + 1
                
            
    
# Generate 2 sorted arrays
one = [random.randint(0, 30) for _ in range(random.randint(5, 10))]
two = [random.randint(0, 30) for _ in range(random.randint(5, 10))]
one.sort();
two.sort();

i, j = 0, 0
three = []
while i < len(one) and j < len(two):
    if one[i] < two[j]:
        three.append(one[i])
        i += 1
    else:
        three.append(two[j])
        j += 1
        
while i < len(one):
    three.append(one[i])
    i += 1

while j < len(two):
    three.append(two[j])
    j += 1

a = Solution()
ans = a.findMedianSortedArrays(one, two)
sol = 0
if len(three) % 2 == 0:
    sol = (three[len(three) // 2] + three[len(three) // 2 - 1]) / 2
else:
    sol = three[(len(three) // 2)]

print(one)
print(two)
print(three)
print("{} : {}".format(ans, sol))
print("Half: {}".format(len(three) // 2))
print(len(three))