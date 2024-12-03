from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = Counter()
        L = 0
        max_freq = 0  # Tracks the count of the most frequent character in the window
        max_length = 0

        for R in range(len(s)):
            char_count[s[R]] += 1
            max_freq = max(max_freq, char_count[s[R]])

            # Check if we need to shrink the window
            if (R - L + 1) - max_freq > k:
                char_count[s[L]] -= 1
                L += 1

            max_length = max(max_length, R - L + 1)

        return max_length
