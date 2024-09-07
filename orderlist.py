from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]):
        #find middle of list
        slow, fast = head, head.next
        if fast == None:
            return
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        #reverse second half of list
        prev, curr = None, slow.next
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        slow.next = None

        #merge lists
        forw, rev, fnext, rnext = head, prev, head.next, prev.next
        while forw != None and rev != None:
            forw.next = rev
            rev.next = fnext
            forw = fnext
            rev = rnext
            fnext = fnext.next if fnext else None
            rnext = rnext.next if rnext else None


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

nums = [1, 2, 3, 4, 5]
head = createList(nums)

a = Solution()
a.reorderList(head)
printList(head)

'''
        # Reverse list
        rev, prev = head, None
        while rev != None:
            temp = rev.next
            rev.next = prev
            prev = rev
            rev = temp
        rev = prev

        fnxt, rnxt = head.next, rev.next
        temp = head
        print("temp")
        printList(temp)
        print("rev")
        printList(rev)
        while temp != None and rev != None:
            temp.next = rev
            rev.next = fnxt
            temp = fnxt
            rev = rnxt
            fnxt = temp.next if temp != None else None
            rnxt = rev.next if rev != None else None

'''
