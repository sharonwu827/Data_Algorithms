#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n =len(nums)
        curPos = 0 
        minSteps = 0
        while curPos<n-1:
            maxLen = nums[curPos]
            if curPos+maxLen>=n-1:
                return minSteps+1  # Add 1 because we jump from nums[curPos] to the last index
            nextPos= curPos
            nextJump = 0 
            for j in range(curPos+1, curPos+maxLen+1):
                if j+nums[j]>nextPos+nextJump:
                    nextPos = j
                    nextJump = nums[j]
            minSteps+=1
            curPos = nextPos
        return minSteps

        
# @lc code=end

