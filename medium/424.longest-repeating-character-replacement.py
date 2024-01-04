#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 窗口长度不固定 需要维持num_changes<=k

        dict_ = {}
        max_len = 0 
        start = 0 
        for end in range(start, len(s)):
            dict_[s[end]] = dict_.get(s[end],0)+1

        # max(dict_.values()): 此时window里面最多的重复元素的数量
        # end-start+1 - max(dict_.values()):剩下不同元素的总数量
            num_changes = end-start+1-max(dict_.values())
            while num_changes>k:
                dict_[s[start]]-=1
                if not dict_[s[start]]:
                    del dict_[s[start]]
                start+=1
            
            max_len = max(max_len, end-start+1)
        
        return max_len
                
# @lc code=end

