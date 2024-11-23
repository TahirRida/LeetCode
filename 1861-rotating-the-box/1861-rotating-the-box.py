class Solution(object):
    def rotateTheBox(self, box):
        """
        :type box: List[List[str]]
        :rtype: List[List[str]]
        """
        m = len(box)      # Number of rows
        n = len(box[0])   # Number of columns

        # Initialize the rotated result matrix
        res = [["."] * m for _ in range(n)]

        # Process each row in the box and simultaneously fill the rotated matrix
        for i in range(m):
            empty = n - 1  # Start from the bottom of the target column
            for j in range(n - 1, -1, -1):
                if box[i][j] == "#":  # Stone
                    res[empty][m - i - 1] = "#"
                    empty -= 1
                elif box[i][j] == "*":  # Obstacle
                    res[j][m - i - 1] = "*"
                    empty = j - 1  # Reset the empty pointer
                else:  # Empty space
                    res[j][m - i - 1] = "."

            # Fill remaining spaces in the rotated matrix with empty cells
            while empty >= 0:
                res[empty][m - i - 1] = "."
                empty -= 1

        return res

                
        