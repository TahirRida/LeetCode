class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(grid, row, col, index):
            if index == len(word):  # If we have matched all characters in word
                return True
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] != word[index]:
                return False

            # Temporarily mark the cell as visited
            temp = grid[row][col]
            grid[row][col] = '#'

            for dx, dy in directions:
                if dfs(grid, row + dx, col + dy, index + 1):
                    return True

            # Restore the cell before backtracking
            grid[row][col] = temp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:  # Start DFS only if first character matches
                    if dfs(board, i, j, 0):  # Pass the index of word
                        return True
        return False
            

        