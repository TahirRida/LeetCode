class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L,length = 0,0
        chars= set()
        for R in range(len(s)):
            while s[R] in chars :
                chars.remove(s[L])
                L+=1
            chars.add(s[R])
            length = max(length,R-L+1)
        return length
            
        
