#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            for j in range(i):
                heapq.heappush(heap, abs(nums[i] - nums[j]))
                if len(heap)>k:
                    heapq.heappop(heap)
       
        return  heapq.heappop(heap)



        

        
# @lc code=end

