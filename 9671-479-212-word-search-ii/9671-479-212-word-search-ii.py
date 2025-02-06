class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Store complete word at the end node

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark the end of a word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        self.result = set()
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(node, row, col):
            char = board[row][col]
            
            node = node.children[char]
            if node.word:  # Found a word
                self.result.add(node.word)

            board[row][col] = "#"  # Mark as visited
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] in node.children:
                    dfs(node, new_row, new_col)
            board[row][col] = char  # Backtrack

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie.root.children:
                    dfs(trie.root, i, j)

        return list(self.result)
