class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in xrange(n-1,-1,-1):
            res += (ord(s[i]) - ord('A') + 1)*(26**(n-i-1))
        return res