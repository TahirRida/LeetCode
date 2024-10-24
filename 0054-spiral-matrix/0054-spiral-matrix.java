class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix == null || matrix.length == 0) return res;
        
        int topRow = 0, bottomRow = matrix.length - 1;
        int leftCol = 0, rightCol = matrix[0].length - 1;
        
        while (topRow <= bottomRow && leftCol <= rightCol) {
            // Traverse from left to right across the top row
            for (int i = leftCol; i <= rightCol; i++) {
                res.add(matrix[topRow][i]);
            }
            topRow++;
            
            // Traverse from top to bottom along the right column
            for (int i = topRow; i <= bottomRow; i++) {
                res.add(matrix[i][rightCol]);
            }
            rightCol--;
            
            // Traverse from right to left across the bottom row (if still valid)
            if (topRow <= bottomRow) {
                for (int i = rightCol; i >= leftCol; i--) {
                    res.add(matrix[bottomRow][i]);
                }
                bottomRow--;
            }
            
            // Traverse from bottom to top along the left column (if still valid)
            if (leftCol <= rightCol) {
                for (int i = bottomRow; i >= topRow; i--) {
                    res.add(matrix[i][leftCol]);
                }
                leftCol++;
            }
        }
        
        return res;
    }
}
