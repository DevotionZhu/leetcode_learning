class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        res = [[1]]
        i = 0
        while i < rowIndex:
            n = len(res[i])
            t = []
            for j in range(n-1):
                t.append(res[i][j] + res[i][j+1])
            res.append(([1]+t+[1]))
            i += 1
        return res[rowIndex]