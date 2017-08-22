class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        r = ''
        s = ''
        table = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        i = 0
        while i < 32:
            t = (num >> i) & 0xf
            if t < 10:
                t = str(t)
            else:
                t = table[t]
            s = t + s
            i += 4

        for v in s:
            if v != '0' or r:
                r += v
        return r if r else '0'