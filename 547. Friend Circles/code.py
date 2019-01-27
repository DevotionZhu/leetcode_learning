
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        m = len(M)
        friend_sets = []
        for i in xrange(m):
            for j in xrange(i+1,m):
                if M[i][j]:
                    new_set = set([i,j])
                    friend_sets.append(new_set)

        n = len(friend_sets)
        i = 0
        while i < n:
            j = i + 1
            flag = True
            while j < n:
                if friend_sets[i] & friend_sets[j]:
                    friend_sets[i] |= friend_sets[j]
                    del friend_sets[j]
                    flag = False
                    n -= 1
                else:
                    j += 1
            if flag:
                i += 1

        num = 0
        tmp = 0
        for v in friend_sets:
            tmp += len(v)
            num += 1

        return num + m - tmp