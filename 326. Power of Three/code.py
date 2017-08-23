import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        x = math.log(n, 3)
        x = int(round(x))
        if n == 3 ** x:
            return True
        return False
