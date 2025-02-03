class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        max_length = 1
        while(i < len(nums)-1):
            curr = 1
            while(i<len(nums)-1 and nums[i]<nums[i+1]):
                i += 1
                curr += 1
                max_length = max(max_length,curr)
                continue
            curr = 1
            while(i<len(nums)-1 and nums[i]>nums[i+1]):
                i+= 1
                curr += 1
                max_length = max(max_length,curr)
            
            while(i<len(nums)-1 and nums[i]==nums[i+1]):
                i += 1
        
        return max_length
            
            
                
            
            




                


        