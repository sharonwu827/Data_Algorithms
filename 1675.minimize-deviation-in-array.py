#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = [] # store original val and the possibel max number the origin val can be
        curMax = 0 
        res = float("inf")

        for num in nums:
            tmp = num
            while num%2 == 0:
                num = num//2
            heapq.heappush(minHeap, (num, max(tmp, 2*num)))
            curMax = max(curMax, num)
        
        while len(minHeap) == len(nums):
            num, maxNum = heapq.heappop(minHeap)
            res = min(res, curMax-num)
            if nu


        

        

                

