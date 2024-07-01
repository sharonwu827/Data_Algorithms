#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i-1] + nums[i-1]
        # HashMap to record the count of prefix sums
        hashmap = defaultdict(int)
        hashmap[0]=1 # initial value

        res = 0 
        for i in range(1, len(preSum)):
            # r = presum[i]
            # l = r - goal
            res += hashmap[preSum[i]- goal]
            hashmap[preSum[i]] += 1
        return res
        

        

# @lc code=end

