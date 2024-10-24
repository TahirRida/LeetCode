class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] rotated = new int[n][n];
        for(int j = 0;j<n;j++){
            for(int i =n-1;i>=0;i--){
                rotated[j][n-1-i] = matrix[i][j];
            }
        }
        for(int j = 0;j<n;j++){
            for(int i =0;i<n;i++){
                matrix[j][i] = rotated[j][i] ;
            }
        }
        
    }
}