class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict = sorted(dict)

        words = sentence.split()
        n = len(words)
        for i in xrange(n):
            for v in dict:
                if words[i][:1] < v[:1]:
                    break
                if words[i].startswith(v):
                    words[i] = v
                    break

        return ' '.join(words)
