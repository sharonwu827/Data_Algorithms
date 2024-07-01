#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        preOddNumber = [1] * (len(nums)+1)
        for i in range(1, len(nums)+1):
            if nums[i-1] % 2 == 1:
                preOddNumber[i] = 1 + preOddNumber[i-1]
            else:
                preOddNumber[i] = preOddNumber[i-1]
        
        res = 1
        for i in range(len(nums)):
            if preOddNumber[i] == k:
                res *= k

        return res
    
# @lc code=end

