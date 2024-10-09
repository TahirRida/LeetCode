class Solution {
    public int maxArea(int[] heights) {
        int left=0;int right=heights.length-1;
        int water=0;
        while(left<right){
            int a = heights[left];
            int b = heights[right];
            int currentWater = (right-left)*Math.min(a,b);
            if(currentWater>water){
                water = currentWater;
            }
            else if(a > b){
                right --;
            }
            else{
                left++;
            }
        }
        return water;

    }
}

