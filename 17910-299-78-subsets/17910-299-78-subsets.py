class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(index, nums, curr, result):
            if index >= len(nums):  
                result.append(curr.copy())  # Append a copy of curr, not a reference
                return  

            # Include lst[index]
            curr.append(nums[index])  
            helper(index + 1, nums, curr, result)  

            # Exclude lst[index]
            curr.pop()  # Corrected: Simply pop the last element
            helper(index + 1, nums, curr, result)  
        result = []  
        curr = []  
        helper(0, nums, curr, result)  
        return result  