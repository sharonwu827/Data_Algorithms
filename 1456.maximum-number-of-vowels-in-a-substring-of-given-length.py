#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = 0
        curVowels = 0
        for i in range(k):
            if s[i] in vowels:
                curVowels += 1
        maxVowels = curVowels
        for i in range(k, len(s)):
            if s[i - k] in vowels and s[i] not in vowels:
                curVowels -= 1
            if s[i - k] not in vowels and s[i] in vowels:
                curVowels += 1
                maxVowels = max(maxVowels, curVowels)
        return maxVowels


# @lc code=end

