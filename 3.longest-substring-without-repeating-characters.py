#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        dict_ = {}
        max_len = 0 
        for right in range(len(s)):
            dict_[s[right]] = dict_.get(s[right], 0)+1
            while len(dict_)<right-left+1:
                dict_[s[left]]-=1
                if not dict_[s[left]]:
                    del dict_[s[left]]
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len


            
   
# @lc code=end

