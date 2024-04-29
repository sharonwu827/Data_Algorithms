#
# @lc app=leetcode id=1449 lang=python3
#
# [1449] Form Largest Integer With Digits That Add up to Target
#

# @lc code=start
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        self.res = 0
        def backtrack(startInd, path, curSum):
            if curSum == target:
                self.res = max(self.res, path.join(""))
                return 
            if cost[startInd]>target:
                return
            
            for i in range(startInd, len(cost)):
                path.append(startInd+1)
                backtrack(startInd+1, )
                path.pop()


            

        
# @lc code=end

