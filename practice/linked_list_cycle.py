class listNode:
    def __init__(self,valor,next = None):
        self.valor = valor
        self.next = next
         
node4  = listNode(5)
node3 = listNode(6)
node2 = listNode(4)
node1 = listNode(7)

node1.next = node3
node3.next = node2
node2.next = node1
node4.next = node3

fast = node1
slow = node1

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        print(True)
        break
else:
    print(False)