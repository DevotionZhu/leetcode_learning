class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        array = []
        for a in A:
            temp = a[::-1]
            array.append([ (0 if a else 1) for a in temp ])
        return array



        //todo