class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')  # Initialize max_sum to negative infinity
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)  # Update current_sum
            max_sum = max(max_sum, current_sum)  # Update max_sum if needed

        return max_sum
            
                
        