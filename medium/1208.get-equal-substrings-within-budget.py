#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#

# @lc code=start
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 窗口不固定 需要维持一个变量
        start = 0
        dict_={}
        max_len = 0
        for end in range(start, len(nums)):
            dict_[nums[end]] = dict_.get(nums[end], 0)+1
            flip_need = dict_.get(0, 0)
            while flip_need > maxCost:
                dict_[nums[start]] -= 1
                start+=1
                flip_need=dict_.get(0, 0)
            max_len = max(max_len, end-start+1)
        return max_len
            
        
# @lc code=end

