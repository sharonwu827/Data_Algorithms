#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        def lcp(left, right):
            if left==right:
                return strs[left]
            mid = left+(right-left)//2
            lcpLeft, lcpRight = lcp(left, mid), lcp(mid + 1, right)
            minLen = min(len(lcpLeft), len(lcpRight))
            for i in range(minLen):
                if lcpLeft[i]!=lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLen]
        return lcp(0, len(strs)-1)


        
            
            



        
# @lc code=end

