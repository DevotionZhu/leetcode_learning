class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0

        res = []
        i = 0
        while i < m+n:
            j = 0
            while j <= i:
                if i&1:
                    if j >= m:
                        break
                    if i-j < n:
                        res.append(matrix[j][i-j])
                    else:
                        j = i - n
                else:
                    if j >= n:
                        break
                    if i-j < m:
                        res.append(matrix[i-j][j])
                    else:
                        j = i - m
                j += 1
            i += 1

        return res