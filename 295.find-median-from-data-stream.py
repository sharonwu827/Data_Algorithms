#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start
class MedianFinder:

    def __init__(self):
        self.largeHeap = [] #  contains the larger half of the numbers,
        self.smallHeap = [] #  contains the smaller half of the numbers,
        

    def addNum(self, num: int) -> None:
        # If the lengths of both heaps are equal
        # moving the smallest element from maxHeap to minHeap
        if len(self.largeHeap) == len(self.smallHeap):
            heapq.heappush(self.largeHeap, num)
            tmp = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -tmp)
        
        else:
            heapq.heappush(self.smallHeap, -num)
            tmp = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, tmp)
        
    def findMedian(self) -> float:
        if len(self.smallHeap) == len(self.largeHeap):
            return (-self.smallHeap[0] + self.largeHeap[0])/2
        else:
            return -self.smallHeap[0]

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

