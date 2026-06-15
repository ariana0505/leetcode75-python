class listnode:
    def __init__(self,valor=0,next=None):
        self.valor=valor
        self.next=next

list1 = listnode(1,listnode(2,listnode(4)))

list2 = listnode(1,listnode(3,listnode(4)))

dummy  =  listnode()

cola = dummy

while list1 != None  and  list2 !=None:
    if  list1.valor >=  list2.valor:
        cola.next = list2
        list2  = list2.next
    else:
        cola.next  = list1
        list1  =  list1.next
    cola = cola.next

if list1 != None:
    cola.next = list1
else:
    cola.next  = list2

resultado =  dummy.next

cur = resultado
while cur:
    print(cur.valor, end="->")
    cur = cur.next