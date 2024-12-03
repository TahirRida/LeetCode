class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        curr_sum = 0
        for R in range(len(arr)):
            if R-L+1 > k:
                curr_sum -= arr[L]
                L += 1
            curr_sum += arr[R]
            if R-L+1 == k :
                if curr_sum/k >= threshold :
                    res += 1

        return res
            