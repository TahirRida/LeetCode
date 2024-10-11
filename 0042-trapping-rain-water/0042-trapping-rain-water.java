class Solution {
    public int trap(int[] heights) {
        int left = 0;
        int right = 1;
        int water = 0;

        while (left < right && right < heights.length) {
            // Move 'right' to find a valid right boundary
            while (right < heights.length && heights[right] < heights[left]) {
                right++;
            }

            // If we reached the end of the array, break
            if (right >= heights.length) {
                break;
            }

            // Calculate the water trapped between left and right
            for (int i = left + 1; i < right; i++) {
                water += Math.max(0, Math.min(heights[left], heights[right]) - heights[i]);
            }

            // Move 'left' to the 'right' and increment 'right'
            left = right++;
        }

        // Handling the case where 'right' goes out of bounds, but there is a plateau on the right
        int maxHeight = heights[heights.length - 1];
        for (int i = heights.length - 2; i >= left; i--) {
            if (heights[i] < maxHeight) {
                water += maxHeight - heights[i];
            } else {
                maxHeight = heights[i];
            }
        }

        return water;
    }
}
