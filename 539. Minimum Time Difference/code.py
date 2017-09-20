class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        n = len(timePoints)
        times = []
        for i in xrange(n):
            th, tm = timePoints[i].split(":")
            times.append([int(th),int(tm)])
        times = sorted(times)
        minute = 1440
        times.append(times[0])
        for i in xrange(n):
            t1h, t1m = times[i]
            t2h, t2m = times[i+1]

            tmp = abs((int(t1h) - int(t2h))*60 +int(t1m) - int(t2m))
            if tmp > 720:
                tmp = 1440 - tmp
            if minute > tmp:
                minute = tmp
            if minute == 0:
                break
        return minute