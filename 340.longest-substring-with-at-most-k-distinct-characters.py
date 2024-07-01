#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dict_ = defaultdict()
        left = 0 
        res = 0
        for right in range(len(s)):
            dict_[s[right]] = dict_.get(s[right], 0)+1
            while len(dict_)>k:
                dict_[s[left]]-=1
                if not dict_[s[left]]:
                    del dict_[s[left]]
                left+=1
            res = max(res, right-left+1)
        return res
        
# @lc code=end

