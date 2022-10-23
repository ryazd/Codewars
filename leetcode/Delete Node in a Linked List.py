# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_n = node.next
        while node_n.next:
            node.val = node_n.val
            node = node.next
            node_n = node_n.next
        node.val = node_n.val
        node.next = None