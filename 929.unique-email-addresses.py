#
# @lc app=leetcode id=929 lang=python3
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmail = set()
        for email in emails:
            cleamMail = []
            for char in email:
                # Stop adding characters to localName.
                if char =='+' or char=='@':
                    break
                # Add this character if not '.'.
                if currChar != '.':
                    cleanMail.append(currChar)
                    

# @lc code=end

