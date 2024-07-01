#
# @lc app=leetcode id=1953 lang=python3
#
# [1953] Maximum Number of Weeks for Which You Can Work
#

# @lc code=start
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxHeap = []
        for i in range(len(milestones)):
            heapq.heappush(maxHeap, (-milestones[i], i))
        res = 0
        while len(maxHeap)>=2:
            freq1, key1 = heapq.heappop(maxHeap)
            freq2, key2 = heapq.heappop(maxHeap)
            res+=2
            if freq1+1<0: 
                heapq.heappush(maxHeap, (freq1+1, key1))
            if freq2+1<0: 
                heapq.heappush(maxHeap, (freq2+1, key2))
        return res+1 if maxHeap else res
    
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        total = sum(milestones)     # 获取任务总数
        most = max(milestones)        # 最大任务数
        rest = total - most   # 其他任务总数
        # 其他任务数 + 1 不超过最多任务，那么只能用其他任务数去插空最大任务数
        # 否则所有任务一定可以互相插空最终完成所有任务
        return 2 * rest + 1 if most >= rest + 1 else total


    