class  ListNode:
    def __init__(self,val,next  = None):
        self.val = val
        self.next =  next

lista = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))

head =  lista
prev  =  None
while head != None:
    temp = head.next
    head.next = prev
    prev = head
    head = temp

imprimir = prev

while imprimir:
    print(imprimir.val ,  end="->")
    imprimir = imprimir.next