from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1, cur2 = l1, l2
        carry = 0
        index = 0
        newNum = ListNode(0)
        temp = newNum
        while cur1 != None or cur2 != None:
            cursum = cur1.val + cur2.val + carry
            carry = cursum - 9 if cursum > 9 else 0
            finaldigit = cursum - 9 if cursum > 9 else cursum
            temp.next = ListNode(finaldigit)
            temp = temp.next

        return newNum.next

def createList(nums: List[int]) -> ListNode:
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    temp = head
    for i in range(1, len(nums)):
        temp.next = ListNode(nums[i])
        temp = temp.next
    return head

def printList(head: ListNode):
    print("----")
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

num1 = [0, 1]
num2 = [0, 2]
ten = createList(num1)
twent = createList(num2)
a = Solution()
res = a.addTwoNumbers(ten, twent)
printList(res)
