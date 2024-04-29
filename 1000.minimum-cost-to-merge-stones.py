#
# @lc app=leetcode id=1000 lang=python3
#
# [1000] Minimum Cost to Merge Stones
#

# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1) % (k-1) != 0:
            return -1
        s = list(accumulate(stones,initial = 0))
        @cache
        def dfs


# @lc code=end

