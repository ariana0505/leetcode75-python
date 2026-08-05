class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next   

lista = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
tail = lista

arr = []
while tail:
    arr.append(tail)
    tail = tail.next

izq,der = 0, len(arr) - 1
while izq < der:
    arr[izq].next = arr[der]
    izq += 1
    if izq == der:
        break
    arr[der].next = arr[izq]
    der -= 1

arr[der].next = None

respuesta = lista
while respuesta:
    print(respuesta.val , end="->")
    respuesta = respuesta.next