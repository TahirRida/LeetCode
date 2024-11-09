import java.util.ArrayList;
import java.util.List;

class Solution {
    public void setZeroes(int[][] matrix) {
        List<Integer> rowsToZero = new ArrayList<>();
        List<Integer> columnsToZero = new ArrayList<>();

        // Identify rows and columns that need to be zeroed
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 0) {
                    if (!rowsToZero.contains(i)) {
                        rowsToZero.add(i);
                    }
                    if (!columnsToZero.contains(j)) {
                        columnsToZero.add(j);
                    }
                }
            }
        }

        // Set entire rows to zero
        for (int i = 0; i < rowsToZero.size(); i++) {
            int row = rowsToZero.get(i);
            for (int j = 0; j < matrix[0].length; j++) {
                matrix[row][j] = 0;
            }
        }

        // Set entire columns to zero
        for (int i = 0; i < columnsToZero.size(); i++) {
            int col = columnsToZero.get(i);
            for (int j = 0; j < matrix.length; j++) {
                matrix[j][col] = 0;
            }
        }
    }
}
