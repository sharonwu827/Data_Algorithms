#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.50%)
# Likes:    11025
# Dislikes: 346
# Total Accepted:    2.8M
# Total Submissions: 4.5M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict_i = {} #O(n) space
        dict_t = {} #O(n) space
        for i in s: #O(n) time
            dict_i[i]=dict_i.get(i,0)+1
        for i in t:
            dict_t[i]=dict_t.get(i,0)+1
        # dict_i = colletions.Counter(s)
        # dict_t = colletions.Counter(t)
        return dict_i==dict_t
            
    
# @lc code=end

