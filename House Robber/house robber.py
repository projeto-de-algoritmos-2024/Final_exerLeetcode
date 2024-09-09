class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursiveRob (i):
            if i >= len(nums):
                return 0
            return max(nums[i]+ recursiveRob(i+2), recursiveRob(i+1))
        result = recursiveRob(0)
        return result