#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysneed(capacity):
            res = 1
            tmp = 0 
            for weight in weights:
                if tmp + weight<=capacity:
                    tmp+=weight
                else:
                    res+=1
                    tmp = weight
            return res
        
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left+(right-left)//2
            # find the min capactiy that <= days
            if daysneed(mid) <= days:
                right = mid
            else:
                left = mid+1
        return left
        
# @lc code=end

