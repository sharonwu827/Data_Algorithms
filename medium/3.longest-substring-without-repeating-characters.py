#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #窗口不固定 需要维持一个条件
        dict_={}
        start = 0 
        max_len = 0
        for end in range(start, len(s)):
            dict_[s[end]] = dict_.get(s[end], 0) + 1
            while end-start+1>len(dict_):
                dict_[s[start]]-=1
                if dict_[s[start]]==0:
                    del dict_[s[start]]
                start+=1
            max_len = max(max_len, end-start+1)
  
        return max_len



            
                    
# @lc code=end

