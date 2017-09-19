class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        times  = {}
        for v in nums:
            if v in times:
                times[v] += 1
            else:
                times[v] = 1

        result = sorted(times.iteritems(), key=lambda x: x[1], reverse=True)

        return [x[0] for x in result[:k]]