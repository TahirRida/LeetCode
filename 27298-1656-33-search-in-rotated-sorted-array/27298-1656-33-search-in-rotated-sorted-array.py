class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Handle edge case of empty array
        if not nums:
            return -1
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # If we found the target, return its index
            if nums[mid] == target:
                return mid
            
            # Check which half is sorted
            # Left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target is in the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        # Target not found
        return -1