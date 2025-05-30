class Solution:
    def canJump(self, nums: List[int]) -> bool:

        reachable = nums[0]
        for i in range(1, len(nums)):
            if reachable < i:
                return False
            reachable = max(reachable, i+nums[i])

        return True