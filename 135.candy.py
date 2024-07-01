#
# @lc app=leetcode id=135 lang=python3
#
# [135] Candy
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        
        left = [0] * n
        for i in range(n):
            if i> 0 and ratings[i]>ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1
        
        right = [1] * n
        for i in range(n-1, -1, -1):
            if i<n-1 and ratings[i]>ratings[i+1]:
                right[i] = right[i+1]+1
            else:
                right[i] = 1
        
        res = 0
        for i in range(n):
            res += max(left[i], right[i])
        return res




        
# @lc code=end

