class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(l, r):
            mid = (l+r) // 2
            
            if l > r:
                return
            
            if nums[mid] == target:
                self.first = min(self.first, mid)
                self.last = max(self.last, mid)
                search(l, mid-1)
                search(mid+1, r)
            elif nums[mid] > target:
                search(l, mid-1)
            else:
                search(mid+1, r)


        self.first, self.last = float('inf'), -1

        r = len(nums)-1
        l = 0
        search(l, r)

        return [self.first if self.first != float('inf') else -1, self.last]