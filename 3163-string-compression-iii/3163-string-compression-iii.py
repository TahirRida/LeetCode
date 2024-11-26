class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        if len(word)==0:
            return ""
        compressed = ""
        i=0
        while(i<len(word)):
            current = 1
            while(i+current<len(word) and current<9 and word[i]==word[i+current]):
                current += 1
            compressed += str(current)+word[i]
            i += current
        return compressed
            