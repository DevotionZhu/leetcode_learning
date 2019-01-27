# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pHead = ListNode(0)
        pHead.next = head
        q = pHead
        if m == n:
            return head

        i = 0
        while i < m:
            p_m = q
            q = q.next
            i += 1

        p = q
        q = q.next
        while i < n:
            t = q.next
            q.next = p
            p = q
            q = t
            i += 1

        p_m.next.next = q
        p_m.next = p

        return pHead.next   
