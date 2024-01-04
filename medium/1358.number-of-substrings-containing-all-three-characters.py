#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dict_= {}
        nums = 0 
        start = 0 
        for end in range(start, len(s)):
            dict_[s[end]] = dict_.get(s[end], 0)+1
            while len(dict_) == 3:
                dict_[s[start]]-=1
                # need to remove the character from the dictionary if its count becomes 0.
                if not dict_[s[start]]:
                    del dict_[s[start]]
                start+=1
                nums += len(s)-end
        return nums
      
# @lc code=end

