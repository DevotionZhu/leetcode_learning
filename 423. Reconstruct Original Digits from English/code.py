class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7',
                'eight':'8', 'nine':'9'}
        flag1 = {'z': 'zero', 'w': 'two','x': 'six', 'u': 'four', 'g': 'eight'}
        flag2 = {'t': 'three', 'f': 'five', 'o': 'one', 's': 'seven'}
        flag3 = {'i': 'nine'}
        letter = {}
        res = ''

        for v in s:
            if v in letter:
                letter[v] += 1
            else:
                letter[v] = 1
        # print letter

        for flag in [flag1, flag2, flag3]:
            for k in flag.keys():
                if k in letter and letter[k]:
                    res += nums[flag[k]]*letter[k]
                    n = letter[k]
                    for v in flag[k]:
                        letter[v] -= n
        res = sorted(res)
        return ''.join(res)
