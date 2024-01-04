#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursNeed(capacity):
            hours_needed = 0
            for pile in piles:
                if pile%capacity==0:
                    hours_needed+=pile//capacity
                else:
                    hours_needed+=pile//capacity+1
            return hours_needed
                    
        
        left = 1
        right = sum(piles)
        while left < right:
            mid = left+(right-left)//2
            # find the min capacity that can eat all the bananas within h
            if hoursNeed(mid) <= h:
                right = mid
            else:
                left = mid+1
        return left
        
        
# @lc code=end

