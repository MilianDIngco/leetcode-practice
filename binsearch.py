from typing import List
import random
def binarySearch(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if target > m:
            l = m + 1
        elif target < m:
            r = m - 1
        else:
            return m
    return -1

success = 0
fail = 0
for index in range(1000):
    arr = [random.randint(0, 500) for x in range(1000)]
    arr.sort()
    target = arr[index]
    res = binarySearch(arr, target)
    if res == -1:
        fail += 1
    else:
        success += 1

print("Success: {} Fail: {}".format(success, fail))