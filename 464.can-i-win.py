#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#

# @lc code=start
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        cache = {}
        # If the maximum choosable integer is greater than or equal to the desired total, 
        # the first player can win immediately
        if maxChoosableInteger >= desiredTotal: return True
        def helper(remaining, chosen):
            if chosen in cache:
                return cache[chosen]
            for i in range(1, maxChoosableInteger+1):
                first = i+helper()
                second = helper(i+1, right)

        return helper(0, maxChoosableInteger)
            
        
# @lc code=end

