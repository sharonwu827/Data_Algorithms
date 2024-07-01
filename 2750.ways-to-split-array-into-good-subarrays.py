#
# @lc app=leetcode id=2750 lang=python3
#
# [2750] Ways to Split Array Into Good Subarrays
#

# @lc code=start
class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        preSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums+1):
            preSum[i] = preSum[i-1] + nums[i-1]
        # HashMap to record the count of prefix sums
        hashmap = defaultdict(int)
        hashmap[0]=1 # initial value

        res = 0 
        for i in range(1, len(preSum)):
            res += hashmap[preSum[i]- 1]
            hashmap[preSum[i]] += 1
        return res

            
        
        
# @lc code=end

