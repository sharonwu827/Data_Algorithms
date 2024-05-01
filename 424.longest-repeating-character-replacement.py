#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_ = defaultdict()
        start = 0 
        maxLen = 0 
        for end, char in enumerate(s):
            dict_[char] = dict_.get(char,0)+1
            while end-start+1  - max(dict_.values()) > k:
                dict_[s[start]]-=1
                start+=1
            if end-start+1 - max(dict_.values()) <=k:
                maxLen = max(maxLen, end-start+1)
        return maxLen
            
                
                


        
# @lc code=end

