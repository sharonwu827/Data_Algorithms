#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarrayNeeded(capacity):
            res = 1 
            tmp = 0
            for num in nums:
                if tmp+num <= capacity:
                    tmp+=num
                else:
                    tmp = num
                    res +=1 
            return res # return based on the capacity, how many subarray needed
        
        left = max(nums)
        right = sum(nums)
        while left<right:
            mid = left+(right-left)//2
            # find the smallest capactity that meet subarrayNeeded = k
            if subarrayNeeded(mid) > k:
                left = mid+1
            else:
                right = mid
        return left
                      
# @lc code=end

