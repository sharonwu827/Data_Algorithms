#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#

# @lc code=start
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heapq.heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heapq.heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heapq.heappush(maxHeap, (-c, 'c'))
        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            #此时的char不能用 需要新的char from heap
            if len(res)>=2 and res[-1] ==res[-2] == char:
                # 如果此时没有多的char 直接return
                if not maxHeap:
                    break
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                if nextFreq+1<0:
                    heapq.heappush(maxHeap, ( nextFreq+1, nextChar))
                heapq.heappush(maxHeap, (freq, char)) # 注意这个条件
            else:
                res.append(char)
                if freq+1<0:
                    heapq.heappush(maxHeap, ( freq+1, char))
        return ''.join(res)

            
    
# @lc code=end

