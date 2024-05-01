#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ = defaultdict()
        start = 0 
        maxLen = 0
        for end in range(len(s)):
            dict_[s[end]]=dict_.get(s[end], 0)+1
            if end-start+1>len(dict_):
                dict_[s[start]]-=1
                if not dict_[s[start]]:
                    del dict_[s[start]]
                start+=1
            if  end-start+1==len(dict_):
                maxLen = max(maxLen, end-start+1)
        return maxLen


            
   
# @lc code=end

