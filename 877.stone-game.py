#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#

# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        cache = {} #@cache
        def helper(left, right):
            # return the number of pile that alice have more than bob
            if left>right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            res = max(piles[left]-helper(left+1, right)
            ,piles[right]-helper(left, right-1))
            cache[(left, right)] = res
            return res
        return helper(0, n-1)>0
            



  
# @lc code=end

