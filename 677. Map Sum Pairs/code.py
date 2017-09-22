class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.table[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        num = 0
        for k, v in self.table.iteritems():
            if k.startswith(prefix):
                num += v
        return num



        # Your MapSum object will be instantiated and called as such:
        # obj = MapSum()
        # obj.insert(key,val)
        # param_2 = obj.sum(prefix)