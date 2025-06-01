from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        dic = defaultdict(set)

        for i in range(1, len(nums)-1):
            l, r = 0, len(nums)-1

            while (l != i and r != i):
                if nums[i] + nums[l] + nums[r] == 0:
                    if (nums[l], nums[r]) not in dic[nums[i]]:
                        ans.append([nums[l],nums[i],nums[r]])
                        dic[nums[i]].add((nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
                    
        return ans