class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    if slow.next:
        slow.next = slow.next.next
    return dummy.next


def values(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    head = ListNode(4, ListNode(5, ListNode(8, ListNode(2))))
    assert values(remove_nth_from_end(head, 2)) == [4, 5, 2]
    head = ListNode(5, ListNode(8, ListNode(2)))
    assert values(remove_nth_from_end(head, 3)) == [8, 2]
    print("4->5->2")
