#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n+1
        while left<right:
            mid = left+(right-left)//2
            if (mid*(mid+1))//2>=n:
                right = mid
            else:
                left = mid+1
        if left*(left+1)//2==n:
            return left
        else:
            return left-1
        
        
# @lc code=end

