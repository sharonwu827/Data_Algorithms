#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x
        while left<right:
            mid = left+(right-left)//2
            if mid**2 > x:
                right = mid
            else:
                left = mid+1
        
        return left-1

        
# @lc code=end

