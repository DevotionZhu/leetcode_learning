class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for v in dict:
            n = len(v)
            if n in self.table:
                self.table[n].append(v)
            else:
                self.table[n] = [v]

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        n = len(word)
        if n in self.table:
            for v in self.table[n]:
                if self.cmp(v, word, n):
                    return True

        return False

    def cmp(self, p, q, n):
        res = 0
        if p == q:
            return False
        for i in range(n):
            if p[i] != q[i]:
                res += 1
            if res > 1:
                return False
        return True



        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)