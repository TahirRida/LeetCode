class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        freq = {}

        # Group numbers by their sum of digits
        for num in nums:
            digit_sum = sum(int(d) for d in str(num))
            if digit_sum in freq:
                freq[digit_sum].append(num)
            else:
                freq[digit_sum] = [num]

        max_sum = -1
        
        # Find max sum of two numbers in the same digit sum group
        for group in freq.values():
            if len(group) > 1:
                group.sort(reverse=True)  # Sort to get the two largest numbers
                max_sum = max(max_sum, group[0] + group[1])  # Sum the two largest

        return max_sum