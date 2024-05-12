#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for c in s:
                # Unicode code point of the character 
                cnt[ord(c)-ord('a')]+=1
            # list cannot be the datatype for key in dict
            res[tuple(cnt)].append(s)
        return res.values()



# @lc code=end

