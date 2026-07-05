class  listNode:
    def  __init__(self, val, next = None):
        self.val   = val
        self.next =  next


lista =  listNode(1,listNode(2,listNode(3,listNode(4))))
prev  = None

head = lista

while head != None:
    temp = head.next
    head.next  = prev
    prev = head
    head = temp

imprimir   = prev

while imprimir != None:
    print(imprimir.val,end="->")
    imprimir = imprimir.next