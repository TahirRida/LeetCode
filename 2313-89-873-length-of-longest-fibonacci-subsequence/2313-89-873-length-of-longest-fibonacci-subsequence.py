class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        if not arr or len(arr) < 3:
            return 0
        
        # Create a set for O(1) lookups
        arr_set = set(arr)
        max_length = 0
        
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                # Start with the first two elements
                a, b = arr[i], arr[j]
                current_length = 2  # Already have 2 elements
                
                # Look for next Fibonacci elements
                while (a + b) in arr_set:
                    # Update to next Fibonacci pair
                    a, b = b, a + b
                    current_length += 1
                
                # Update max_length if we found a sequence of at least 3 elements
                if current_length >= 3:
                    max_length = max(max_length, current_length)
        
        return max_length

                