#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        memo = {}
        def dfs(num):
            if num not in nums:
                return 0
            if num in memo:
                return memo[num]
            one = dfs(num+1)
            second = dfs(num-1)
            curMax = max(one, second)+num
            memo[num] = curMax
            return curMax
        res = -float('inf')
        for num in nums:
            res = max(res, num)
        return res



class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        rows = len(costs)
        cols = len(costs[0])
        cache = {}
        def dfs(row, col):
            # return the mincost at (row, col)
            # base case 
            # Base case: no more houses to paint, cost is 0
            if row == rows:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            minCost = float('inf')
            for i in range(3): # only three colors
                if i!=col:
                    remaining = dfs(row+1, i)
                    minCost = min(minCost, remaining+costs[row][col])
            cache[(row, col)] = minCost
            return minCost
    
        # Return the minimum cost from the first row
        minCost = float('inf')
        for i in range(cols):
            minCost = min(minCost, dfs(0, i))
        return minCost


            
        



    
# @lc code=end

