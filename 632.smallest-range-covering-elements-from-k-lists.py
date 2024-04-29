#
# @lc app=leetcode id=632 lang=python3
#
# [632] Smallest Range Covering Elements from K Lists
#

# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 从 k个列表中各取一个数，使得这 k 个数中的最大值与最小值的差最小。

        minHeap = [] #heap store value, index, 当前所在的row index
        curMax = -float("inf")
        start = 0 
        end = float('inf')

        for i in range(len(nums)):
            heapq.heappush(minHeap, (nums[i][0], 0, i)) 
            curMax = max(curMax, nums[i][0])  
        
        while len(minHeap) ==len(nums):
            # pop curMin
            val, ind, rowInd = heapq.heappop(minHeap)
            if end - start > curMax - val: 
                start = val
                end = curMax
            if ind < len(nums[rowInd])-1:
                heapq.heappush(minHeap, (nums[rowInd][ind+1], ind+1, rowInd)) 
                curMax = max(curMax, nums[rowInd][ind + 1]) 
        return [start, end]


            

            

        
# @lc code=end

