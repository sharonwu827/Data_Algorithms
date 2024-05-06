#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        # Add imaginary balloons at the beginning and end
        nums = [1] + nums + [1]
        cache = {}
        # @cache
        def helper(left, right):
            if left>right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            res = 0
            for i in range(left+1, right):
                tmp = nums[left] * nums[i] * nums[right]
                tmp+= helper(left, i)+helper(i, right)
                res = max(res, tmp)
            cache[(left, right)] = res
            return res
        return helper(0, n+1)

        
# @lc code=end
