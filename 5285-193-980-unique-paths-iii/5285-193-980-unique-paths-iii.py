class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        # let s find the index of the starting and ending point and count obstacles
        start_r = 0
        start_c = 0
        obstacles = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 :
                    start_r = r
                    start_c = c
                if grid[r][c] == -1 :
                    obstacles += 1
        visited = set()
        def dfs(r,c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r,c) in visited or grid[r][c] == -1 :
                return 0
            if grid[r][c] == 2 and len(visited) == ROWS*COLS - obstacles - 1:
                return 1
            visited.add((r,c))
            count = 0
            for nr,nc in directions:
                count += dfs(r+nr,c+nc)
            visited.remove((r,c))
            return count
        return dfs(start_r,start_c)
