class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        curr_sum = sum(arr[:k])  # Compute the initial window sum
        threshold_sum = threshold * k  # Convert threshold to sum for easier comparison

        # Check the first window
        if curr_sum >= threshold_sum:
            res += 1

        # Slide the window
        for R in range(k, len(arr)):
            curr_sum += arr[R] - arr[R - k]  # Update the sliding window sum
            if curr_sum >= threshold_sum:
                res += 1

        return res
