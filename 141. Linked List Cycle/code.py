# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        m = head
        n = m.next
        while n:
            t = n.next
            if t == head:
                return True
            n.next = m
            m = n
            n = t
        return False        