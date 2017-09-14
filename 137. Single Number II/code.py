class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit32 = [0]*32
        for num in nums:
            i = 0
            while i < 32:
                bit32[i] += (num>>i) & 1
                i += 1
        res = 0
        for i in xrange(32):
            bit32[i] %= 3
            if bit32[i]:
               res += 1<<i
        if res >= 2147483648:
            # res = ~((~res)&(0xFFFFFFFF))
            res = ~(res^(0xFFFFFFFF))
        return res    
