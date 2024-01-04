#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(dict_t, dict_s):
            for i in dict_t:
                if i not in dict_s or dict_s[i]<dict_t[i]:
                    return False
            return True
        
        # 窗口长度不固定
        # when t all in the window, move the start pointer
        dict_t = {}
        dict_s = {}
        min_len = float("inf")
        start = 0 
        res = ""
        for ch in t:
            dict_t[ch] = dict_t.get(ch,0)+1
        
        for end in range(start, len(s)):
            dict_s[s[end]] = dict_s.get(s[end],0)+1
            
            while helper(dict_t, dict_s):
                # 更新答案后在move start
                if min_len > end-start+1:
                    min_len = end-start+1
                    res = s[start:end+1]
                
                dict_s[s[start]]-=1
                if not dict_s[s[start]]:
                    del dict_s[s[start]]
                start+=1

        return res
         
# @lc code=end