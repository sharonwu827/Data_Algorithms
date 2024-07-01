#
# @lc app=leetcode id=2461 lang=python3
#
# [2461] Maximum Sum of Distinct Subarrays With Length K
#

# @lc code=start
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        dict_= defaultdict(int)
        maxSum = 0 
        left = 0 
        n = len(nums)
        curSum = 0 

        for right in range(n):
            curSum+=nums[right]
            dict_[nums[right]] = dict_.get(nums[right], 0)+1
            # we have duplicate
            while right-left+1>len(dict_):
                dict_[nums[left]]-=1
                if not dict_[nums[left]]:
                    del dict_[nums[left]]
                curSum-=nums[left]
                left+=1

            if right-left+1 > k:
                dict_[nums[left]]-=1
                curSum-=nums[left]
                if not dict_[nums[left]]:
                    del dict_[nums[left]]
                left+=1
            if right-left+1 == k:
                maxSum = max(maxSum, curSum)

        return maxSum
            
       
# @lc code=end

