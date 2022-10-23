class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_L(self):
        m = self
        while m.next:
            print(m.val)
            m = m.next
        print(m.val)


def oddEvenList(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    odd1 = head
    a = head.next
    while a and a.next:
        even1 = odd1.next
        odd1.next = a.next
        odd1 = odd1.next
        a.next = odd1.next
        odd1.next = even1
        a = a.next
    return head
