#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_ = defaultdict()
        left = 0
        res = 0 
        for right in range(len(s)):
            dict_[s[right]] = dict_.get(s[right], 0)+1
            # minFrequency = min(dict_.values())
            # print(minFrequency)
            # # 不能这么写 因为可能更换两个不一样的字母
            # if len(dict_)>1 and minFrequency > k:
            if right-left+1 - max(dict_.values())>k:
                dict_[s[left]]-=1
                if not dict_[s[left]]:
                    del dict_[s[left]]
                left+=1
            res = max(res, right-left+1)
        return res
        
        
# @lc code=end

