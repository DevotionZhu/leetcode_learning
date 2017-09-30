class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        a,b,_,c,d = time
        num = sorted([a,b,c,d])
        for v in num:
            if v > d:
                return "%s%s:%s%s" %(a,b,c,v)
        for v in num:
            if v <= '5' and v > c:
                return "%s%s:%s%s" %(a, b, v,num[0])
        for v in num:
            if a <= '1' and v > b:
                return "%s%s:%s%s" %(a, v, num[0], num[0])
            if a == '2' and v <= '4' and v > b:
                return "%s%s:%s%s" %(a,v,num[0],num[0])
        for v in num:
            if v <= '2' and v > a:
                return "%s%s:%s%s" %(v, num[0], num[0],num[0])
        return "%s%s:%s%s" %(a,a,a,a)