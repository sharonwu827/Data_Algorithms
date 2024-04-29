#
# @lc app=leetcode id=2963 lang=python3
#
# [2963] Count the Number of Good Partitions
#

# @lc code=start
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:


        
        
# @lc code=end

class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        dict_ = {}
        left = 0 
        right = 0 
        numString = 0
        for right in range(len(s)):
            dict_[s[right]] = dict_.get(s[right], 0)+1
            while right-left+1>len(dict_):
                dict_[s[left]]-=1
                if not dict_[s[left]]:
                    del dict_[s[left]]
                left+=1
            numString += right-left+1
        return numString
        
                