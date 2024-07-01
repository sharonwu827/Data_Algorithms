#
# @lc app=leetcode id=2398 lang=python3
#
# [2398] Maximum Number of Robots Within Budget
#

# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        ans = s = left = 0
        q = deque()
        # 枚举区间右端点 right，计算区间左端点 left 的最小值
        for right, (t, c) in enumerate(zip(chargeTimes, runningCosts)):
            # 及时清除队列中的无用数据，保证队列的单调性
            while q and t >= chargeTimes[q[-1]]:
                q.pop()
            q.append(right)
            s += c
            # 如果左端点 left 不满足要求，就不断右移 left
            while q and chargeTimes[q[0]] + (right - left + 1) * s > budget:
                # 及时清除队列中的无用数据，保证队列的单调性
                if q[0] == left:
                    q.popleft()
                s -= runningCosts[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans


        
# @lc code=end

