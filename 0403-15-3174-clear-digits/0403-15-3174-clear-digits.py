class Solution:
    def clearDigits(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if '0'<=s[i]<='9':
                result = result[:len(result)-1]
                continue
            result += s[i]
        return result
        