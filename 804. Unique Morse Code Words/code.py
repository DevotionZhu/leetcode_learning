class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.",
                 "--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = set()
        for word in words:
            tmp = ""
            for letter in word:
                index = ord(letter) - ord('a')
                tmp += table[index]
            alphabet.add(tmp)
        return len(alphabet)