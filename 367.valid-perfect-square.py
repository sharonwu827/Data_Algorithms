#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num//2
        while left<right:
            mid = left+(right-left)//2
            if mid**2>=num:
                right=mid
            else:
                left = mid+1
        return left**2 == num      
# @lc code=end

