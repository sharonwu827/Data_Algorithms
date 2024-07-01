#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def sumOfArray(value):
            # return the sum 
            # after change all the integers > value to be equal to value
            curSum = 0 
            for num in arr:
                if num > value:
                    curSum += value
                else:
                    curSum+=num
            return curSum
        
        left = 0
        right = max(arr)
        while left<=right:
            mid = left+(right-left)//2
            if sumOfArray(mid)>=target:
                right=mid-1
            else:
                left = mid+1
        if sumOfArray(left)==10:
            return left
        elif abs(sumOfArray(left)-10) < abs(sumOfArray(left-1)-10):
            return left
        else:
            return left-1

        



        
# @lc code=end

