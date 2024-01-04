#
# @lc app=leetcode id=1300 lang=python3
#
# [1300] Sum of Mutated Array Closest to Target
#

# @lc code=start
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def getNewSum(k):
            # smaller k, small sum
            res = 0
            for num in arr:
                res += min(k, num)
            return res
        
        left = 0
        right = max(arr)
        while left<right:
            mid = left+(right-left)//2
            # find the first number makes the getNewSum >= target
            if getNewSum(mid)>=target: 
                # we need lower the newSum
                right = mid
            else:
                left = mid+1

        # 单调递增 min abs different comes from left or left-1
        case_1 = getNewSum(left)
        case_2 = getNewSum(left-1)

        if abs(case_1-target)<abs(case_2-target):
            return left
        else:
            return left-1
        

              
# @lc code=end

