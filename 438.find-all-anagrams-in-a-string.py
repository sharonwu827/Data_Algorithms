#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_s = {}
        dict_p = {}
        res = []
        left =0 
        right = 0 
        for char in p:
            dict_p[char] = dict_p.get(char, 0)+1

        for right in range(len(s)):
            dict_s[s[right]] = dict_s.get(s[right], 0)+1
            if dict_s == dict_p:
                res.append(left)
            if right-left+1>=len(p):
                dict_s[s[left]]-=1
                if not  dict_s[s[left]]:
                    del dict_s[s[left]]
                left+=1
        return res
                
        
# @lc code=end

