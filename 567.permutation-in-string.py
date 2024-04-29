#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
    
        dict_s1 = {} 
        dict_s2 = {}
        for i in s1:
            dict_s1[i] = dict_s1.get(i, 0)+1

        left = 0 
        for right in range(len(s2)):
            dict_s2[s2[right]] = dict_s2.get(s2[right], 0)+1
            if dict_s2 == dict_s1:
                return True
            #  ensure that the window size is the same as the size of s1
            if right-left+1 >= len(s1): 
                dict_s2[s2[left]]-=1
                if not dict_s2[s2[left]]:
                    del dict_s2[s2[left]]
                left+=1

        return False
                

# @lc code=end

