class Solution {
    public int findMin(int[] nums) {
        int low = 0;
        int high = nums.length - 1;

        // If the array is already sorted (no rotation)
        if (nums[low] < nums[high]) {
            return nums[low];
        }

        // Binary search to find the point of rotation
        while (low < high) {
            int mid = low + (high - low) / 2;

            // If mid element is greater than the high element, 
            // the minimum is on the right side
            if (nums[mid] > nums[high]) {
                low = mid + 1;
            }
            // Otherwise, the minimum is on the left side
            else {
                high = mid;
            }
        }

        // When low == high, we have found the smallest element
        return nums[low];
    }
}
