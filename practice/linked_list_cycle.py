class ListNode:
    def __init__(self, valor = 0, next = None):
        self.valor = valor
        self.next = next

node4 =  ListNode(3)
node3 =  ListNode(5)
node2 = ListNode(6)
node1 = ListNode(8)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

slow =  node1
fast = node1


while fast and fast.next:
    slow = slow.next
    fast  = fast.next.next
    if slow == fast:
        print(True)
        break
else:
    print(False)
