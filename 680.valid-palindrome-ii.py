#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValidPalindrome(left, right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                else:
                    left+=1
                    right-=1
            return True
                
        left = 0 
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                option1 = isValidPalindrome(left+1, right)
                option2 = isValidPalindrome(left, right-1)
                return option1 or option2
            else:
                left+=1
                right-=1
        return True

        
        
# @lc code=end

