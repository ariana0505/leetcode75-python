class ListNode:
    def __init__(self, valor = 0,next =None):
        self.valor =  valor
        self.next = next

node4 =  ListNode(3)
node3 = ListNode(4,node4)
node2 = ListNode(5, node3)
node1 = ListNode(8, node2)
node4.next = node3

slow =  node1
fast = node1

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow  == fast:
        print(True)
        break
else:
    print(False)