class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)) :
            a = nums[i]
            if target - a in map :
                return [i,map[target-a]]
            map[a]=i
        return 0
        