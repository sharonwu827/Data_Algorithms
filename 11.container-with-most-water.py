#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        max_area = -float('inf')
        while left<right:
            cur_area = (right-left) * min(height[right], height[left])
            if cur_area>max_area:
                max_area = cur_area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area



                

        
# @lc code=end

