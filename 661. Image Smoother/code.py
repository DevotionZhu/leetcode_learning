class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        if M:
            n = len(M[0])
        res = [[[0] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                tmp = 0
                num = 0
                for x in range(i-1,i+2):
                    for y in range(j-1,j+2):
                        if 0 <= x < m and 0 <= y < n:
                            tmp += M[x][y]
                            num += 1
                res[i][j] = tmp/num

        return res