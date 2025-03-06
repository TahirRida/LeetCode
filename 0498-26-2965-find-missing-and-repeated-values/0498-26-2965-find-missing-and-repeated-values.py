class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        res = [i for i in range(1,n*n+1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] in res:
                    res.remove(grid[i][j])
                else:
                    res = [grid[i][j]]+res
        return res