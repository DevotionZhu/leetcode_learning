class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s = len(s)
        len_t = len(t)
        i = 0
        j = 0
        while i < len_t and j < len_s:
            if t[i] == s[j]:
                j += 1

            i += 1

        if j < len_s:
            return False
        return True