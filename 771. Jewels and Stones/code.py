class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = set(J)
        num = 0
        for s in S:
            if s in jewels:
                num += 1
        return num