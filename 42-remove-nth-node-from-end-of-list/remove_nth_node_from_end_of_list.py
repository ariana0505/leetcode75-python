class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

node =  ListNode(4)
node2 = ListNode(5)
node3 = ListNode(8)
node4 = ListNode(2)

node.next = node2
node2.next =   node3
node3.next =  node4

fast = node
slow = node

n = 3
resul = []

for _  in range(n):
    if  fast != None:
        fast = fast.next
    else:
        print(resul)

resul.append(slow.val)  # agregamos el primer nodo antes de mover

while slow.next != None:
    if fast != None:
        slow = slow.next
        fast = fast.next
        if fast != None:       # solo agrega si NO es el nodo a eliminar
            resul.append(slow.val)
    else:
        slow = slow.next       # salta el nodo eliminado (antes era .next.next, saltaba de mas)
        while slow != None:    # agrega los nodos restantes
            resul.append(slow.val)
            slow = slow.next
        break

print(resul)
