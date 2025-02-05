class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        diff1 = []
        diff2 = []
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff1.append(s1[i])
                diff2.append(s2[i])
            if len(diff1)>2:
                return False
        return sorted(diff1)==sorted(diff2)

        