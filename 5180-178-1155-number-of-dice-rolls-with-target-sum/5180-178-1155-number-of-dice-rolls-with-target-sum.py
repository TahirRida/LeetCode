from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        
        @lru_cache(None)
        def helper(dice, curr_sum):
            if dice == n:  
                return 1 if curr_sum == target else 0  
            if curr_sum > target:  
                return 0  

            ways = 0
            for i in range(1, k + 1):  
                ways = (ways + helper(dice + 1, curr_sum + i)) % MOD  

            return ways  
        
        return helper(0, 0) 
