#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysNeeded(capacity):
            daysNeeded = 1
            curCapacity = 0
            for weight in weights:
                if curCapacity+weight<=capacity:
                    curCapacity+=weight
                else:
                    daysNeeded+=1
                    curCapacity = weight # 注意这里不是curCapacity = 0
            return daysNeeded
        
        left = max(weights) # 注意这里不是 left = min(weights)
        right = sum(weights)
        while left<right:
            mid = left+(right-left)//2
            if daysNeeded(mid)<=days: # 注意这里不是 daysNeeded(mid)<days
                right = mid
            else:
                left = mid+1
        return left

            
# @lc code=end

