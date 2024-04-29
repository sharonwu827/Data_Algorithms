#
# @lc app=leetcode id=871 lang=python3
#
# [871] Minimum Number of Refueling Stops
#

# @lc code=start
import heapq
from typing import List

import heapq
from typing import List

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target, 0))
        curPos = 0
        curFuel = startFuel
        numRefuel = 0 
        maxHeap = []

        for pos, fuel in stations:
            # Drive to the station
            curFuel-=pos-curPos
            # If the car can't reach the station with current fuel
            while curFuel<0 and maxHeap:
                # Refuel by taking fuel from the previous largest station
                curFuel += -heapq.heappop(maxHeap)
                numRefuel += 1
            # If still cannot reach, return -1
            if curFuel<0:
                return -1
            # Add the station's fuel to the priority queue
            heapq.heappush(maxHeap, -fuel)
            curPos = pos
        return numRefuel

# Example usage:

            