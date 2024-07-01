#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        res = 0 
        for i, h in enumerate(height):
            while stack and height[stack[-1]]<h:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                right = i
                curWidth = right-left-1
                curHeight = min(min(height[left], h))-height[top]
                res += curWidth*curHeight
            stack.append(i)
        return res

        
# @lc code=end

