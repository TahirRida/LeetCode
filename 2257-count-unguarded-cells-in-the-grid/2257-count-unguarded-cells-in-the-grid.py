class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        # Initialize the grid
        grid = [[0] * n for _ in range(m)]  # 0 for unguarded cells
        for x, y in walls:
            grid[x][y] = 2  # 2 represents walls
        for x, y in guards:
            grid[x][y] = 3  # 3 represents guards

        # Directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Mark guarded cells
        for x, y in guards:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                while 0 <= nx < m and 0 <= ny < n:
                    # Stop if we hit a wall or another guard
                    if grid[nx][ny] == 2 or grid[nx][ny] == 3:
                        break
                    if grid[nx][ny] == 0:  # Mark as guarded
                        grid[nx][ny] = 1
                    nx += dx
                    ny += dy

        # Count unguarded cells
        unguarded_count = sum(row.count(0) for row in grid)
        return unguarded_count

                