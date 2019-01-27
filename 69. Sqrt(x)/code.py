class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 :
            return 0

        x0 = float(x)/2
        while True:
            x1 = x0
            x0 = (x0 + x/x0)/2
            if x1 - x0 < 1:
                break

        return int(x0)
