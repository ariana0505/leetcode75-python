import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

listas = [list1, list2, list3]
heap = []

for i,lista in enumerate(listas):
    if lista:
        heapq.heappush(heap,(lista.val,i, lista))

dummy = ListNode()
tail = dummy

while heap:
    extraido = heapq.heappop(heap)
    val , i , nodo = extraido
    if nodo.next:
        heapq.heappush(heap,(nodo.next.val, i, nodo.next))
    tail.next = nodo
    tail = tail.next

respuesta = dummy.next
while respuesta:
    print(respuesta.val, end="->")
    respuesta = respuesta.next