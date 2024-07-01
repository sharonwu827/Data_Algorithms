#
# @lc app=leetcode id=2841 lang=python3
#
# [2841] Maximum Sum of Almost Unique Subarray
#

# @lc code=start
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        dict_ = defaultdict(int)
        left = 0 
        curSum = 0
        maxSum = 0 
        for right in range(len(nums)):
            curSum+=nums[right]
            dict_[nums[right]] = dict_.get(nums[right], 0)+1
            
            # while right-left+1>m and len(dict_) < m:
            #     curSum-= nums[left]
            #     dict_[nums[left]]-=1
            #     if not dict_[nums[left]]:
            #         del dict_[nums[left]]
            #     left+=1

            if right-left+1 == k:
                if len(dict_) >=m:
                    maxSum = max(maxSum, curSum)
                curSum-= nums[left]
                dict_[nums[left]]-=1
                if not dict_[nums[left]]:
                    del dict_[nums[left]]
                left+=1
        return maxSum
  
# @lc code=end

