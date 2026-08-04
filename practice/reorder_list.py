class ListNode:
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next

lista = ListNode(1,ListNode(4,ListNode(5,ListNode(6,ListNode(9,ListNode(10))))))
rama = lista

arr = []

while rama:
    arr.append(rama)
    rama = rama.next

izq , der = 0, len(arr) - 1
while izq < der:
    arr[izq].next = arr[der]
    izq += 1
    if izq == der:
        break
    arr[der].next = arr[izq]
    der -= 1

arr[der].next = None