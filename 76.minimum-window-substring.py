#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # check every character in t (including duplicates) is included in the window of s
        def includeT(dict_t, dict_s):
            for char in dict_t:
                if char not in dict_s:
                    return False
                if dict_t[char]>dict_s[char]:
                    return False
            return True
        
        dict_t = defaultdict()
        dict_s = defaultdict()
        start = 0 
        minLen = float("inf")
        startInd = 0 

        for char in t:
            dict_t[char] = dict_t.get(char, 0)+1
    
        for end, char in enumerate(s):
            dict_s[char] = dict_s.get(char, 0)+1
            # 这里在已经满足条件的情况下继续移动右指针没有意义
            while includeT(dict_t, dict_s):
                if minLen>end-start+1:
                    minLen = end-start+1
                    startInd = start
                dict_s[s[start]]-=1
                if not dict_s[s[start]]:
                    del dict_s[s[start]]
                start+=1
        return s[startInd: startInd + minLen] if minLen != float("inf") else ""

       