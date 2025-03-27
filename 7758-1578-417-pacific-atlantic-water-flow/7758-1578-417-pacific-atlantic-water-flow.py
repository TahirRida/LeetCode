class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def bfs(r, c, ocean):
            q = deque([(r, c)])
            visited = set()
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                
                # If we've reached the ocean, return True
                if ocean == "Pacific" and (row == 0 or col == 0):
                    return True
                if ocean == "Atlantic" and (row == rows - 1 or col == cols - 1):
                    return True

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols:  # Valid cell
                        if (nr, nc) not in visited and heights[nr][nc] <= heights[row][col]:
                            visited.add((nr, nc))
                            q.append((nr, nc))
            
            return False
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c, "Pacific") and bfs(r, c, "Atlantic"):
                    res.append([r, c])
                    
        return res