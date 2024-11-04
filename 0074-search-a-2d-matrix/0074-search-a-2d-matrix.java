class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = 0;
        int low = 0;
        int high = matrix[0].length -1;
        while(matrix[row][high]<target){
            if(row + 1 < matrix.length){
                row++;
            }
            else{
                return false;
            }
        }
        int[] nums = matrix[row];
        while(low <= high){
            int mid = (low + high)/2;
            if(nums[mid] == target){
                return true;
            }
            if(nums[mid]>target){
                high = mid -1;
            }
            if(nums[mid]<target){
                low = mid + 1;
            }
        }
        return false;
    }
}
