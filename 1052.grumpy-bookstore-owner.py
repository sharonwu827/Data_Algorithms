#
# @lc app=leetcode id=1052 lang=python3
#
# [1052] Grumpy Bookstore Owner
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # find consecutive array that have at most minutes grumpy time and have the largest sum
        left = 0 
        curGrumpyTime = 0 
        curSum = 0
        res = 0 
        for right in range(len(customers)):
            if grumpy[right]==0:
                curGrumpyTime+=1
            if curGrumpyTime <= minutes:
                curSum+=customers[right]
                res = max(res, curSum)
            while curGrumpyTime >= minutes:
                curSum-=customers[left]
                left+=1
                curGrumpyTime-=1
        return res
            
            
        
# @lc code=end

