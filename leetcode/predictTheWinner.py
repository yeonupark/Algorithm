class Solution:
    def predictTheWinner(self, nums):

        def choose(nums, turn = True):
        
            if len(nums) < 3:
                if turn:
                    return max(nums)
                else:
                    return min(nums)
                
            if turn:
                return max(nums[0] + choose(nums[1:], False), nums[-1] + choose(nums[:len(nums)-1], False))
            else:
                return min(choose(nums[1:], True), choose(nums[:len(nums)-1], True))

        return sum(nums) - choose(nums)*2 <= 0