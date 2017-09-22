class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        tables = [-1]*n
        none_set = set()
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                tables[i] = nums[i+1]
                # remove
                remove_set = set()
                for j in none_set:
                    if nums[j] < nums[i+1]:
                        tables[j] = nums[i+1]
                        remove_set.add(j)
                none_set -= remove_set
            else:
                none_set.add(i)


        none_set.add(n-1)
        for i in none_set:
            for j in range(i):
                if nums[j] > nums[i]:
                    tables[i] = nums[j]
                    break

        return tables