#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDistance(x, y):
            return (x**2+y**2)**0.5
        
        heap = []
        for point in points:
            distance = getDistance(point[0], point[1])
            heapq.heappush(heap, (distance,point[0], point[1]))
        res = []
        for _ in range(k):
            distance, x, y = heapq.heappop(heap)
            res.append([x,y])
        return res

        
# @lc code=end

