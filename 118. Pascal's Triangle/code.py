class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        i = 0
        while i < numRows-1:
            n = len(res[i])
            t = []
            for j in range(n-1):
                t.append(res[i][j] + res[i][j+1])
            res.append(([1]+t+[1]))
            i += 1
        return res