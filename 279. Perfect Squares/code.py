class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square = []
        for i in xrange(1,n+1):
            if i**2 > n:
                break
            square.append(i**2)

        nums = [0]*(n+1)
        for i in xrange(1,n+1):
            if i in square:
                nums[i] = 1
            else:
                x = 65535
                for j in square:
                    if i < j:
                        break
                    t = nums[i-j] + nums[j]
                    if x > t:
                        x = t
                nums[i] = x

        return nums[n]  
