#
# @lc app=leetcode id=2643 lang=python3
#
# [2643] Row With Maximum Ones
#

# @lc code=start
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        res = 0 
        maxOnes = -float('inf')
        for i in range(rows):
            if sum(mat[i]) > maxOnes:
                maxOnes = sum(mat[i])
                res = i
        return [res, maxOnes]

        
        
        
# @lc code=end

