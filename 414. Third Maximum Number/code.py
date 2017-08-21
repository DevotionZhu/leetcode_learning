class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nlargest = []
        for n in nums:
            if n not in nlargest:
                nlargest.append(n)
                nlargest = sorted(nlargest, reverse=True)
                if len(nlargest) > 3:
                    nlargest.pop()
        if len(nlargest) < 3:
            return nlargest[0]
        return nlargest.pop()