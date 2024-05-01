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

        start = 0 
        for end, char in enumerate(s2):
            dict_s2[char] = dict_s2.get(char, 0)+1
            while end-start+1 > len(s1): 
                dict_s2[s2[start]]-=1
                if dict_s2[s2[start]] == 0:
                    del dict_s2[s2[start]] 
                start+=1
            if end-start+1 == len(s1) and dict_s2 == dict_s1:
                return True
        return False
                

# @lc code=end

