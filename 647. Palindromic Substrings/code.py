class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        num = 0
        for length in xrange(n):
            for start in xrange(n-length):
                tmp = s[start:start+length+1]
                if tmp == tmp[::-1]:
                    num += 1
        return num