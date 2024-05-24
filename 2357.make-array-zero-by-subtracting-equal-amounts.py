#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsSet = set()
        for num in nums:
            if num != 0:
                numsSet.add(num)
        return len(numsSet)


        
# @lc code=end

