
class listNode:
    def __init__(self,valor, next= None):
        self.valor =  valor
        self.next = next

node1 = listNode(1)
node2 = listNode(3)
node3 =  listNode(4)
node4 = listNode(6)
node1.next  = node2
node2.next = node3
node3.next = node4
node4.next = node2

slow  = node1
fast = node1

while fast and fast.next:
    slow =  slow.next
    fast =  fast.next.next

    if slow  == fast:
        print(True)
        break
else:
    print(False)