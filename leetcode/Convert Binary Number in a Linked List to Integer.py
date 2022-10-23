# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getDecimalValue(head: ListNode) -> int:
    b = []
    b.append(head.val)
    while head.next:
        head = head.next
        b.append(head.val)
    return int(''.join(map(str, b)), base=2)



