class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum = 0
        min_abs_value = float('inf')  # Initialize with a large value
        negative_count = 0

        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                value = matrix[i][j]
                total_sum += abs(value)  # Add the absolute value to the total sum
                min_abs_value = min(min_abs_value, abs(value))  # Update the smallest absolute value
                if value < 0:
                    negative_count += 1  # Count the number of negative numbers

        # If the count of negatives is odd, subtract twice the smallest absolute value
        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_value

        return total_sum
