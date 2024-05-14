#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_ = defaultdict()
        for num in nums:
            dict_[num]= dict_.get(num, 0)+1
        return max(dict_.keys(), key=dict_.get)


        
# @lc code=end

