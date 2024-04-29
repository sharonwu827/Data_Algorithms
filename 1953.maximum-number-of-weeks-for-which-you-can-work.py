#
# @lc app=leetcode id=1953 lang=python3
#
# [1953] Maximum Number of Weeks for Which You Can Work
#

# @lc code=start
class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        maxHeap = []
        total_milestones = sum(milestones)
        for i in range(len(milestones)):
            heapq.heappush(maxHeap, (-milestones[i], -i)) # store (-milestone, project)
        res = 0
        
        while len(maxHeap)>=2:
            milestone1, project1 = heapq.heappop(maxHeap)
            milestone2, project2 = heapq.heappop(maxHeap)
            res+=2
            if -milestone1>1:
                heapq.heappush(maxHeap, (milestone1+1, project1))
            if -milestone2>1:
                heapq.heappush(maxHeap, (milestone2+1, project2))
        
        return res+1 if maxHeap else res
            
            
        
# @lc code=end

