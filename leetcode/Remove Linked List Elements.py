# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        lst = []
        if head:
            if head.val != val:
                lst.append(head.val)
            while head.next:
                head = head.next
                if head.val != val:
                    lst.append(head.val)
        if lst:
            lst.reverse()
            h = ListNode(lst[0])
            for i in range(1, len(lst)):
                h = ListNode(lst[i], h)
            return h
        if head:
            return head.next
        return head