class Solution:
    def mySqrt(self, x: int) -> int:
        first = 0
        last = x
        while first <= last:
            mid = (first + last) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                first = mid + 1
            else:
                last = mid - 1
        
        return last