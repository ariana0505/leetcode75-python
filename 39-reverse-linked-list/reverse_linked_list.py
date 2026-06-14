class listnode:
    def  __init__(self,valor , next = None):
        self.valor = valor
        self.next = next

node1 = listnode(1)
node2 = listnode(2)
node3 = listnode(3)
node4 = listnode(4)
node5 = listnode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node = node1
prev = None
while node:
    siguiente  =  node.next
    node.next = prev
    prev = node
    node =  siguiente

cur = prev

while cur:
    print(cur.valor, end="->")
    cur = cur.next