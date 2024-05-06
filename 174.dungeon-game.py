#
# @lc app=leetcode id=174 lang=python3
#
# [174] Dungeon Game
#

# @lc code=start
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # 备忘录中都初始化为 -1
        memo = [[-float("inf") for _ in range(n)] for _ in range(m)]

        return self.dp(grid, 0, 0, memo)

    # 备忘录，消除重叠子问题
    def dp(self, grid: List[List[int]], i: int, j: int, memo: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # base case
        if i == m - 1 and j == n - 1:
            return 1 if grid[i][j] >= 0 else -grid[i][j] + 1
        if i == m or j == n:
            return float('inf')
        # 避免重复计算
        if memo[i][j] != -float("inf"):
            return memo[i][j]
        # 状态转移逻辑
        res = min(
                self.dp(i, j + 1),
                self.dp(i + 1, j)
            ) - grid[i][j]
        # 骑士的生命值至少为 1
        memo[i][j] = 1 if res <= 0 else res

        return memo[i][j]

            
            

        
# @lc code=end

