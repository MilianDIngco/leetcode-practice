from typing import List
import math

'''
RELATIONSHIP BETWEEN TIME TO EAT AND EATING SPEED IS INVERSE
as eating speed decreases, time to eat increases
'''

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeToEat(piles: List[int], k: int) -> int:
            res = 0
            for i in piles:
                res += math.ceil(float(i) / k)
            return res
        
        piles.sort()
        l, r, m, ans = 1, piles[-1], 0, 0
        
        while l <= r:
            m = l + ((r - l) // 2)
            tte = timeToEat(piles, m)
            print("m: {} tte: {}".format(m, tte))
            
            if tte <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
            
            
    
a = Solution()
piles=[30,11,23,4,20]
h=6
print(a.minEatingSpeed(piles, h))

'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r, ans, prev = 0, len(piles) - 1, 0, 0
        
        while l <= r:
            prev = ans
            ans = l + ((r - l) // 2)
            time = ans + 1
            for i in range(ans + 1, len(piles)):
                time += (math.ceil(piles[i] / piles[ans]))

            print("H: {} TIME: {} ANS: {}".format(h, time, piles[ans]))
            
            if h < time:
                l = ans + 1
            elif h > time:
                r = ans - 1
            else: 
                return piles[ans]
            
        return piles[prev] 
'''