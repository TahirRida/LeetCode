class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        Prefix =strs[0]
        for i in range(1,len(strs)):
            k = 0
            for j in range(min(len(strs[i]),len(strs[i-1]))):
                if(strs[i][j]==strs[i-1][j]):
                    k += 1
                    continue
                break
            if (k == 0):
                return ""
            if(k>len(Prefix)):
                continue
            Prefix = strs[i][:k]
        return Prefix
                    
                
            
        