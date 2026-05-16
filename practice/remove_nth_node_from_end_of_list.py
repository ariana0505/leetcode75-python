class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

slow = node1
fast = node1

n = 2
for _ in range(n):
    fast = fast.next

while fast.next != None:
    slow = slow.next
    fast = fast.next

slow.next = slow.next.next

node = node1
while node != None:
    print(node.val, end="->")
    node = node.next
