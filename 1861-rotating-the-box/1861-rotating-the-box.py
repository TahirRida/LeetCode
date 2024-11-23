class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(box)      # Number of rows
        n = len(box[0])   # Number of columns
        
        # Apply gravity to each row of the box
        for i in range(m):
            empty = n - 1  # Start from the rightmost column
            for j in range(n - 1, -1, -1):
                if box[i][j] == "#":  # Stone
                    box[i][j], box[i][empty] = box[i][empty], box[i][j]
                    empty -= 1
                elif box[i][j] == "*":  # Obstacle
                    empty = j - 1

        # Rotate the box 90 degrees clockwise
        res = [[None] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][m - i - 1] = box[i][j]
        
        return res

                
                
        