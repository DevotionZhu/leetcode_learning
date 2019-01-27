class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cycle_sets = set()
        for num in nums:
            if num in cycle_sets:
                continue
            tmp_set = set([num])
            while True:
                if nums[num] not in tmp_set:
                    tmp_set.add(nums[num])
                    num = nums[num]
                else:
                    break
            if res < len(tmp_set):
                res = len(tmp_set)
            cycle_sets |= tmp_set
        return res