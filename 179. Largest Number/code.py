class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        res = []
        length = 0
        for v in nums:
            flag = True
            for i in range(length):
                if self.mycmp(str(v), str(res[i])):
                    res.insert(i, str(v))
                    flag = False
                    break
            if flag:
                res.append(str(v))
            length += 1
        if res[0] == '0':
            return "0"
        return "".join(res)

    def mycmp(self, a, b):
        if int(a + b) > int(b + a):
            return True
        return False