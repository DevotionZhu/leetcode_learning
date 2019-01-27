# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = []
        num2 = []
        len1 = 0
        len2 = 0
        tmp = l1
        while tmp:
            len1 += 1
            num1.append(tmp.val)
            tmp = tmp.next
        tmp = l2
        while tmp:
            len2 += 1
            num2.append(tmp.val)
            tmp = tmp.next


        if len1 > len2:
            res = num1[:len1-len2]
            for i in xrange(len2):
                res.append(num1[len1-len2+i] + num2[i])
        else:
            res = num2[:len2-len1]
            for i in xrange(len1):
                res.append(num1[i] + num2[len2-len1+i])
        head = None
        flag = False
        for v in res[::-1]:
            if flag:
                v += 1
            if v < 10:
                tmp = ListNode(v)
                flag = False
            else:
                tmp = ListNode(v - 10)
                flag = True
            tmp.next = head
            head = tmp
        if flag:
            tmp = ListNode(1)
            tmp.next = head
            head = tmp
        return head