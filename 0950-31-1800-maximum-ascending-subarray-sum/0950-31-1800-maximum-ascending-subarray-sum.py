class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        i = 0
        while(i<len(nums)):
            curr = 0
            while(i<len(nums)-1 and nums[i]<nums[i+1]):
                curr += nums[i]
                i += 1
            curr+=nums[i]
            i += 1
            max_sum = max(max_sum,curr)
        return max_sum
        