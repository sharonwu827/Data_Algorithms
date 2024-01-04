#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # set up the boundary to include all possible elements;
        left = 1
        right = n
        
        while left < right:
            mid = left+(right-left)//2
            if not isBadVersion(mid):
                left = mid+1
            else:
                right = mid
        return left
        
# @lc code=end

