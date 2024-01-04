#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return the start indice
        # 窗口固定 ，需要满足条件 helper is true, len(p) = end-start+1

        def helper(dict_p, dict_s):
            if i in dict_p:
                if i not in dict_s or dict_s[i]<dict_p[i]:
                    return False
            return True
        
        res = []
        dict_p = {}
        for i in p:
            dict_p[i] = dict_p.get(i,0)+1
        
        dict_s = {}
        start = 0 
    
        for end in range(start, len(s)):
            dict_s[s[end]] = dict_s.get(s[end],0)+1

            while end-start+1>len(p):
                dict_s[s[start]]-=1
                if not dict_s[s[start]]:
                    del dict_s[s[start]]
                start+=1

            if dict_s==dict_p:
                res.append(start)
        return res

               
# @lc code=end

