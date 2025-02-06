class Solution:
    def tupleSameProduct(self,nums)->int:
        product_map = defaultdict(int)  # Dictionary to store product counts
        count = 0  # To count valid tuples
        
        # Generate all unique pairs and count occurrences of each product
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                count += 8 * product_map[product]  # Each existing pair forms 8 valid (a, b, c, d) tuples
                product_map[product] += 1  # Store the pair occurrence
        
        return count