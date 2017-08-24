class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        while True:
            n -= int(9*i*(10**(i-1)))
            if n <= 0 :
                break
            i += 1
        n += int(9*i*(10**(i-1)))
        if i == 1:
            x = int(n/i)
        else:
            x = int(10**(i-1) + (n-1)/i)

        index = (n-1)%i

        x = str(x)
        return int(x[index])