#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = Counter(nums) #0(n)
        minHeap = []

        for key, val in dict_.items():
            heapq.heappush(minHeap, (val, key)) #O(logN)
            while len(minHeap)>k:
                heapq.heappop(minHeap) #O(logN)
        res = []
        for _ in range(len(minHeap)):
            res.append(heapq.heappop(minHeap)[1])
        return res
        
        
            
        



        
# @lc code=end

