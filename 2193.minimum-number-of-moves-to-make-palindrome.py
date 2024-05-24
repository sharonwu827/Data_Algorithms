#
# @lc app=leetcode id=2193 lang=python3
#
# [2193] Minimum Number of Moves to Make Palindrome
#

# @lc code=start
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        @cache
        def dfs(s: str) -> int:
            n = len(s)
            if n <= 1:
                return 0
            for i in range(n - 1):
                if s[i] == s[-1]:
                    return i + dfs(s[:i] + s[i + 1 : -1])
            for i in range(n - 1, 0, -1):
                if s[i] == s[0]:
                    return n - 1 - i + dfs(s[1:i] + s[i + 1 :])
            return -1

        return dfs(s)

        
# @lc code=end

