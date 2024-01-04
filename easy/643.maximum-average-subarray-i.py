#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -float("inf")
        cur_sum = 0
        start = 0 
        for end in range(start, len(nums)):
            cur_sum+= nums[end]
            while end-start+1>k :
                cur_sum-= nums[start]
                start+=1
            # 因为窗口固定，需要在满足条件的时候update max_sum
            if end-start+1==k:
                max_sum = max(max_sum, cur_sum)
        return max_sum/k


        
# @lc code=end

