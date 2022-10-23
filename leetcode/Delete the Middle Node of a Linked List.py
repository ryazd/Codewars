# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        length = 1
        while cur.next:
            length += 1
            cur = cur.next
        if length == 1:
            return None
        cur = head
        cur_2 = head.next.next
        for i in range(0, length // 2 - 1):
            cur = cur.next
            cur_2 = cur_2.next
        cur.next = cur_2
        return head