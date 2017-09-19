class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_i = m
        min_j = n
        for v in ops:
            i, j = v
            if min_i > i:
                min_i = i
            if min_j > j:
                min_j = j
        return min_i*min_j