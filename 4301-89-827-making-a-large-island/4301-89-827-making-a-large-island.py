class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island_id = 2  # Unique ID for each island (starting from 2 to avoid confusion with 1s & 0s)
        island_sizes = {0: 0}  # Maps island_id to its area
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4 directions
        
        def dfs(r, c, id_):
            """ Perform DFS and mark all connected cells with island_id """
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return 0
            
            grid[r][c] = id_
            size = 1  # Current cell
            for dr, dc in directions:
                size += dfs(r + dr, c + dc, id_)
            return size
        
        # Step 1: Identify all islands and store their sizes
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # Found an unvisited island
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1  # Move to the next island
        
        # Step 2: Try flipping each `0` to `1` and compute the largest possible island
        max_island = max(island_sizes.values(), default=0)  # Max existing island
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:  # Only check `0` cells
                    seen_islands = set()
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 1:
                            seen_islands.add(grid[nr][nc])  # Track unique islands
                    
                    # Compute new island size by merging adjacent islands
                    new_size = 1 + sum(island_sizes[i] for i in seen_islands)
                    max_island = max(max_island, new_size)
        
        return max_island
