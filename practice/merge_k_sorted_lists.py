import heapq

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

list1 = ListNode(1,ListNode(3,ListNode(5)))
list2 = ListNode(3,ListNode(4,ListNode(7)))
list3 = ListNode(4,ListNode(6,ListNode(8)))
lists = [list1,list2,list3]

heap = heapq
heap = []

dummy = ListNode()
cola = dummy


for i,lista in enumerate(lists):
    if lista:
        heapq.heappush(heap,(lista.val, i , lista))

while heap:
    extraido = heapq.heappop(heap)
    val , i , nodo = extraido
    cola.next = nodo
    cola = cola.next
    if nodo.next:
        heapq.heappush(heap, (nodo.next.val, i , nodo.next))

recorrer = dummy.next

while recorrer:
    print(recorrer.val , end="->")
    recorrer = recorrer.next