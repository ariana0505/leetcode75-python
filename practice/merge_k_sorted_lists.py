import heapq
class ListNode:
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next

lista1 = ListNode(1,ListNode(4,ListNode(5)))
lista2 = ListNode(1,ListNode(3,ListNode(4)))
lista3 = ListNode(2,ListNode(6))

listas = [lista1, lista2,lista3]
heap = []
dummy = ListNode()
tail = dummy
#(lista.val, next , lista)
for i, lista in enumerate(listas):
    heapq.heappush(heap,(lista.val, i , lista))

while heap:
    extraido = heapq.heappop(heap)
    val , i , nodo = extraido
    if nodo.next:
        heapq.heappush(heap,(nodo.next.val, i , nodo.next))
    tail.next = nodo
    tail = tail.next

resultado = dummy.next

cur = resultado
while cur:
    print(cur.val, end="->")
    cur = cur.next
print("None")
