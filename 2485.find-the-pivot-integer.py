#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 1
        right = n
        total_sum = n*(n+1)/2
        while left < right:
            mid = left + (right - left) // 2
            if mid*(mid+1) == total_sum + mid:
                return mid
            elif mid*(mid+1) > total_sum + mid:
                right = mid-1
            else:
                left = mid+1
        return -1
            

                 
# @lc code=end

