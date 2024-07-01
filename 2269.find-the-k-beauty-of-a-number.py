#
# @lc app=leetcode id=2269 lang=python3
#
# [2269] Find the K-Beauty of a Number
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        kBeauty = 0
        numStr = str(num)
        for i in range(len(numStr)-k+1):
            if int(numStr[i:i+k])!=0 and num%int(numStr[i:i+k])==0:
                kBeauty += 1
        return kBeauty

                      
        
# @lc code=end

