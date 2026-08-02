class listNode:
    def __init__(self,val, next = None):
        self.val = val
        self.next = next

lista = listNode(1,listNode(2,listNode(3,listNode(4,listNode(5)))))
head = lista
arr = []

while lista:
    arr.append(lista)
    lista = lista.next

l , r = 0 , len(arr) - 1

while l < r:
    arr[l].next = arr[r]
    if l+1 == r:
        break
    arr[r].next = arr[l+1]
    l+=1
    r-=1

arr[r].next = None

result = []
node = head
while node:
    result.append(node.val)
    node = node.next
print(result)

