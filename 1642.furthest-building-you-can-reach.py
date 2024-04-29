#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = [] # store 梯子跨越的建筑物高度差
        for i in range(1, len(heights)):
            diff = heights[i]-heights[i-1]
            # the current building's height >= the next building's height
            # no action needed
            if diff<=0:
                continue
            # the current building's height < the next building's height
            # and we need to use ladder or bricks
            else:
                heapq.heappush(heap, diff)
                # ladders-=1 ## cannot have it here, we cannot using the ladders before checking if there are enough ladders available
                #  check if the number of height differences stored exceeds # of ladders
                if len(heap) > ladders:
                    past_max_diff=-heapq.heappop(heap)
                    bricks+=past_max_diff
                if bricks<0:
                    return i-1 
        return len(heights)-1
# @lc code=end

