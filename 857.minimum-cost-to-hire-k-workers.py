#
# @lc app=leetcode id=857 lang=python3
#
# [857] Minimum Cost to Hire K Workers
#
import heapq
# @lc code=start
class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        eff = []
        heap
        for i in range(len(quality)):
            rate = wage[i]/quality[i]
            eff.append(rate, quality[i], wage[i])
        # Sort workers based on wage/quality ratio
        eff.sort(key=lambda a:-a[0])
        # Min heap to store quality values
        minHeap = []
        
        for i in range(k):
            heapq.heappush(minHeap, -quality[eff[i]])
            sum_q += quality[worker[i]]





            

            
            
            







        
# @lc code=end

