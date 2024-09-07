from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for _ in range(n):
            end = end.next
        temp = ListNode(0, head)
        start = temp
        while end != None:
            start = start.next
            end = end.next
        start.next = start.next.next
        return temp.next

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


a = Solution()

nums = [1]
head = createList(nums)
printList(head)

temp = a.removeNthFromEnd(head, 1)
printList(temp)
