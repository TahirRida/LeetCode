class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Iterate through the list and trim the prefix
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Trim the last character
                if not prefix:       # If prefix becomes empty
                    return ""
        
        return prefix
