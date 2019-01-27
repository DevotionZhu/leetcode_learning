class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        tmp = []
        for v in ops:
            if v == 'C':
                tmp.pop()
            elif v == 'D':
                tmp.append(tmp[-1]*2)
            elif v == '+':
                tmp.append(tmp[-1] + tmp[-2])
            else:
                tmp.append(int(v))
        return sum(tmp)