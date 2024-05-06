#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # curPos = 0
        # while curPos < n-1:
        #     maxLen = nums[curPos]
        #     if curPos + maxLen >= n-1:
        #         return True
        #     # Initialize nextPos to current position
        #     nextPos = curPos 
        #     # Initialize nextJump length
        #     nextJump = 0  
        #     for j in range(curPos, curPos+maxLen+1):
        #         if j+nums[j]>nextPos+nextJump:
        #             nextPos = j
        #             nextJump = nums[j]
        #     # If no position is reachable, return False
        #     if nextPos == curPos:
        #         return False
        #     curPos = nextPos
        # return curPos>=n-1
        n = len(nums)
        nextPos, end, step = 0, 0, 0
        for i in range(n-1):
            if nextPos>=i:
                nextPos = max(*m)




  
# @lc code=end

