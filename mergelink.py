from typing import Optional
from typing import List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2

        if temp1 == None and temp2 != None:
            return temp2
        elif temp1 != None and temp2 == None:
            return temp1
        elif temp1 == None and temp2 == None:
            return None
    
        res = None
        if temp1.val < temp2.val:
            res = temp1
            temp1 = temp1.next
        else:
            res = temp2
            temp2 = temp2.next

        temp = res
        while (temp1 != None and temp2 != None):
            if temp1.val < temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next

        temp.next = temp1 or temp2

        return res 

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

one = []
two = []
num1 = createList(one)
printList(num1)
num2 = createList(two)
printList(num2)

a = Solution()
res = a.mergeTwoLists(num1, num2)
printList(res)
