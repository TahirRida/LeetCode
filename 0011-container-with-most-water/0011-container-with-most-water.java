class Solution {
    public int maxArea(int[] height) {
        int maxArea = 0; // To store the maximum area found
        int left = 0; // Starting from the leftmost line
        int right = height.length - 1; // Starting from the rightmost line

        while (left < right) {
            // Calculate the current area between left and right lines
            int currentArea = Math.min(height[left], height[right]) * (right - left);
            // Update maxArea if currentArea is larger
            maxArea = Math.max(maxArea, currentArea);

            // Move the pointer of the shorter line inward
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea;
    }
}
