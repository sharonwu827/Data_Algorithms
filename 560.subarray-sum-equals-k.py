#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum = [0] * (len(nums) + 1)
        for i in range(1, len(preSum)):
            preSum[i] = preSum[i-1] + nums[i-1]
        hashmap = defaultdict(int)
        hashmap[0]=1
        res = 0 
        for i in range(1, len(preSum)):
            right = preSum[i] 
            left  = right - k
            res+= hashmap[left]
            hashmap[right] += 1
        return res
            
        
# @lc code=end

