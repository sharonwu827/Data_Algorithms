#
# @lc app=leetcode id=2781 lang=python3
#
# [2781] Length of the Longest Valid Substring
#

# @lc code=start

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        s = set(forbidden)
        left = 0   # 窗口左端点
        res = 0 # 最终结果
        for right in range(len(word)):
            for i in range(right, max(right - 10, left - 1), -1):
                if word[i: right + 1] in s: # 匹配到屏蔽词，左端点右移，将屏蔽词移出窗口
                    left = i + 1
                    break
            res = max(res, right - left + 1)
        return res     

