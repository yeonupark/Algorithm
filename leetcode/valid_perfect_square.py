class Solution:
    
    def isPerfectSquare(self, num: int) -> bool:
        
        top = num//2 + 1
        bottom = 0

        while bottom <= top:

            mid = (top+bottom) // 2

            if mid*mid == num:
              return True

            elif mid*mid > num:
                top = mid - 1

            else:
                bottom = mid + 1

        return False