class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []  # List to build the resulting string
        for char in s:
            # Add the current character only if the last two characters are not the same as the current one
            if len(result) < 2 or not (result[-1] == char and result[-2] == char):
                result.append(char)
        return ''.join(result)  # Convert the list back to a string
        
            

        