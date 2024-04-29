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
            n = len(res)
            # 违反连续三个字符相同：该字符无法加到答案，
            # 从堆中取出剩余次数次大的字符
            if n>=2 and res[n-1]==res[n-2]==char:
                if not maxHeap:
                    break
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                if -nextFreq>1: 
                    heapq.heappush(maxHeap, (nextFreq+1, nextChar))
                heapq.heappush(maxHeap, (freq, char))
            else:
                res.append(char)
                if -freq>1: 
                    heapq.heappush(maxHeap, (freq+1, char))

        return ''.join(res)

        
# @lc code=end

