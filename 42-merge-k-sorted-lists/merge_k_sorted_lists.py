import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

heap = []
dummy = ListNode()
tail = dummy

for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, (node.val, i, node))

while heap:
    val, index, node = heapq.heappop(heap)
    tail.next = node
    tail = tail.next
    if node.next:
        heapq.heappush(heap, (node.next.val, index, node.next))

result = dummy.next

cur = result
while cur:
    print(cur.val, end="->")
    cur = cur.next
print("None")
