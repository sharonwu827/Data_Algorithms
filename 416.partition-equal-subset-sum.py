#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        cache = {}  # Initialize the cache dictionary

        def memorization(i, curSum):
            if (i, curSum) in cache:
                return cache[(i, curSum)]

            if curSum == target:
                return True

            if i == n:
                return False

            include = memorization(i + 1, curSum + nums[i])
            exclude = memorization(i + 1, curSum)
            
            if include:
                cache[(i, curSum)] = True
            cache[(i, curSum)] = exclude

            return cache[(i, curSum)]

        return memorization(0, 0)

    
        
