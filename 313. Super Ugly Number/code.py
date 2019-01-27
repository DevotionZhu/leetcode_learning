class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res = [1]
        m = len(primes)
        index = [0]*m
        tmp = [0]*m
        i = 0
        while i < n:
            for j in xrange(m):
                tmp[j] = primes[j]*res[index[j]]
            small = min(tmp)
            res.append(small)
            for j in xrange(m):
                if small == primes[j]*res[index[j]]:
                    index[j] += 1
            i += 1
        return res[n-1]
