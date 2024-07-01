#
# @lc app=leetcode id=2340 lang=python3
#
# [2340] Minimum Adjacent Swaps to Make a Valid Array
#

# @lc code=start
class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        if n ==1:
            return 0
        maxInd=0
        minInd=0 
        for i in range(n):
            if nums[i] >= nums[maxInd]:
                maxInd = i
            if nums[i] < nums[minInd]:
                minInd = i

        if maxInd<minInd:
            # mean if we moove maxInd, the minind will change
            # moveMax = n-1-maxInd
            # moveMin = minInd-1
            return (n-1-maxInd)+(minInd-1)
        if maxInd>minInd:
            return minInd+(n-1-maxInd)

           
            
        
        
# @lc code=end

