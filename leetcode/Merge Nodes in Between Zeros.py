# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sum_lst = []
        cur = head
        while cur.next:
            lst = []
            cur = cur.next
            while cur.val != 0:
                lst.append(cur.val)
                cur = cur.next
            sum_lst.append(sum(lst))
        sum_lst.reverse()
        head = ListNode(sum_lst[0])
        for i in range(1, len(sum_lst)):
            head = ListNode(sum_lst[i], head)
        return head