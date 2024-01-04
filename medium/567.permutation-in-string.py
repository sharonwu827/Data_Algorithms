#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #窗口固定 len(s1) 维持一个定量 dict_s1 ==dict_s2
        dict_s1 = {} 
        dict_s2 = {}
        for i in s1:
            dict_s1[i] = dict_s1.get(i, 0)+1

        start = 0 
        for end in range(start, len(s2)):
            dict_s2[s2[end]] = dict_s2.get(s2[end], 0)+1

            while end-start+1>len(s1):
                dict_s2[s2[start]] -= 1
                if  dict_s2[s2[start]]==0:
                    del dict_s2[s2[start]]
                start+=1
            
            if dict_s1 ==dict_s2:
                return True
              
        return False
                  
# @lc code=end

