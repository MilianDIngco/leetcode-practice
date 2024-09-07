from typing import Optional, List
import random

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        #Hashmap to keep track of indices
        randmap = {None:None}

        cur = head
        while cur != None:
            randmap[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur != None:
            randmap[cur].next = randmap[cur.next]
            randmap[cur].random = randmap[cur.random]
            cur = cur.next

        return randmap[head]

def createList(nums: List[int]) -> Node:
    if len(nums) == 0:
        return None
    head = Node(nums[0])
    nums[0] = head
    temp = head
    for i in range(1, len(nums)):
        temp.next = Node(nums[i])
        nums[i] = temp.next
        temp = temp.next
    return head
    
def printList(head: Node):
    print("----")
    temp = head
    while temp:
        if temp.random != None:
            print("{} {}".format(temp.val, temp.random.val))
        else:
            print(temp.val)
        temp = temp.next

a = Solution()
num = [3, 7, 4, 5]
rand = [-1, 3, 0, 1]
head = createList(num)
for i in range(len(num)):
    num[i].random = num[rand[i]] if rand[i] != -1 else None

num[0].random = None
newhead = a.copyRandomList(head)
printList(head)
printList(newhead)
