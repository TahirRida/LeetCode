class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # Dictionary to store the last index of each character
        L = 0  # Left pointer
        max_length = 0  # Length of the longest substring

        for R in range(len(s)):
            if s[R] in char_index and char_index[s[R]] >= L:
                L = char_index[s[R]] + 1  # Move left pointer to avoid repeating characters
            char_index[s[R]] = R  # Update the last seen index of the character
            max_length = max(max_length, R - L + 1)  # Update the maximum length

        return max_length

            
        
