class Solution(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        if(n == 0 or edges == [[]]):
            return -1
        strong = [i for i in range(n)]
        for i in range(len(edges)):
            if edges[i][1] in strong : 
                strong.remove(edges[i][1])
        if len(strong) != 1:
            return -1
        return strong[0]

            
        