#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        p1 = 1
        p2 = 2
        for i in range(3, n+1):
           p3 = p2+p1
           p1 = p2
           p2 = p3
        return p3
    
            

         
     
# @lc code=end

