#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # need to group by anagrams, but no idea how many
        dict_ = {} # dict usually used for anagrams
        for str in strs:
            tmp = ''.join(sorted(str))
            if tmp not in dict_:
                dict_[tmp] = [str]
            else:
                dict_[tmp].append(str)
        return dict_.values()

            
            

        
# @lc code=end

