class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        if n <= 0:
            return res
        num = 1 << (n-1)
        while True:
            x = res[-1]
            i = 0
            while i < 32:
                tmp = x ^ (1<<i)
                if tmp not in res:
                    res.append(tmp)
                    break
                i += 1
            if res[-1] == num:
                break
        return res