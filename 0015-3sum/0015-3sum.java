class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);  // Step 1: Sort the array
        List<List<Integer>> res = new ArrayList<>();
        
        for (int i = 0; i < nums.length - 2; i++) {
            // Step 2: Skip duplicate numbers for i to avoid duplicate triplets
            if (i > 0 && nums[i] == nums[i - 1]) continue;
            
            int left = i + 1;
            int right = nums.length - 1;
            
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                
                if (sum == 0) {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    // Step 3: Move the left and right pointers to avoid duplicates
                    while (left < right && nums[left] == nums[left + 1]) left++;
                    while (left < right && nums[right] == nums[right - 1]) right--;
                    
                    left++;
                    right--;
                } else if (sum < 0) {
                    left++;  // Increase the sum
                } else {
                    right--;  // Decrease the sum
                }
            }
        }
        
        return res;
    }
}
