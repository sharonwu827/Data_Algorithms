#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def numOfArrar(minSum):
            # return number of subarray needed
            curSum = nums[0] 
            numOfArrar = 0 
            for num in nums[1:]:
                if curSum+num<=minSum:
                    curSum+=num
                else:
                    numOfArrar+=1
                    curSum = num
            return numOfArrar

        left = max(nums)
        right = sum(nums)
        while left<=right:
            mid = left+(right-left)//2
            if numOfArrar(mid)>k:
                left = mid+1
            else:
                right = mid-1
        return left-1
            
       