class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

node =  ListNode(4)
node2 = ListNode(5)
node3 = ListNode(8)
node4 = ListNode(2)

node.next = node2
node2.next =   node3
node3.next =  node4

fast = node
slow = node

n = 2

for _ in  range(n):
    fast  =  fast.next

while not fast.next == None:
    fast =  fast.next
    slow = slow.next

slow.next   =  slow.next.next

cur  = node

while cur:
    print(cur.val , end="->")
    cur  = cur.next
    