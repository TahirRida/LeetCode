class Solution {
    public int maxArea(int[] heights) {
        int left=0;int right=heights.length-1;
        int water=0;
        while(left<right){
            int currentWater = (right-left)*Math.min(heights[left],heights[right]);
            if(currentWater>water){
                water = currentWater;
            }
            else if(heights[left] > heights[right]){
                right --;
            }
            else{
                left++;
            }
        }
        return water;

    }
}

