#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # find whether dict_s include all the characters in t
        def check(dict_s, dict_t):
            for item, val in dict_t.items():
                if item not in dict_s or dict_s[item]<val:
                    return False
            return True
                    
        left = 0
        right = 0
        dict_t = {}
        for i in t:
            dict_t[i] = dict_t.get(i, 0) + 1
        dict_s = {}
        found = 0
        min_len = float("inf")
        res = ''

        if len(t) > len(s):
            return ""
        
        for right in range(len(s)):
            dict_s[s[right]] = dict_s.get(s[right], 0)+1
            if s[right] in dict_t and dict_t[s[right]] == dict_s[s[right]]:
                found+=1
            # 这里在已经满足条件的情况下继续移动右指针没有意义
            while check(dict_s, dict_t):
                if min_len > right-left+1:
                    res = s[left:right+1]
                    min_len = right-left+1
                dict_s[s[left]]-=1
                if s[left] in dict_t and dict_t[s[left]] > dict_s[s[left]]:
                    found-=1
                left+=1
           
        return res
                
                

       