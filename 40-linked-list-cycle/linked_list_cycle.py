class ListNode:
    def  __init__(self,valor: int,next = None):
        self.valor = valor
        self.next = next

nodo1 = ListNode(4)
nodo2 = ListNode(6)
nodo3 = ListNode(8)
nodo4 = ListNode(6)

nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4
nodo4.next = nodo2

slow = nodo1
fast = nodo1
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        print(True)
        break
else:
    print(False)