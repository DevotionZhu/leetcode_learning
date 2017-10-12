class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre = n & 1
        n >>= 1
        while n:
            now = n & 1
            if now == pre:
                return False
            pre = now
            n >>= 1
        return True