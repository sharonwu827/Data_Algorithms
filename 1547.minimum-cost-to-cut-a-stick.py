#
# @lc app=leetcode id=1547 lang=python3
#
# [1547] Minimum Cost to Cut a Stick
#

# @lc code=start
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cache = {}
        def helper(left, right):
            # between left and right, inclusively
            # the minimum total cost of the cuts
            if right-left<=1:
                return 0
            if (left,right) in cache:
                return cache[(left,right)]
            res = float('inf')
            for cut in cuts:
                if left<cut<right:
                    res = min(res, (right-left)+helper(left, cut)+helper(cut, right))
            if res == float('inf'):
                res = 0 
            cache[(left,right)] = res
            return res
        return helper(0, n)
