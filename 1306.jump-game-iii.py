#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#

# @lc code=start
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        curPos = start
        while curPos<n-1:
            maxLen = arr[curPos]
            if curPos+maxLen >=n-1:
                return True
            nextPos = curPos
            nextJump = 0 

            lowerBound = min(0, curPos-maxLen)
            maxBound = max(n-1, curPos+maxLen+1)
            for i in range(lowerBound, maxBound):
                if 


        
        
# @lc code=end

