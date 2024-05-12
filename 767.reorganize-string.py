#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#

# @lc code=start
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = []
        maxFreq = -float("inf")
        for char, freq in freq.items():
            heapq.heappush(maxHeap, (-freq, char))
            maxFreq = max(maxFreq, freq)
        # good to have
        if maxFreq>(len(s)+1)//2:
            return ''
        
        res = []
        prevChar = None
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            # we need a new char
            if prevChar and prevChar == char:
                if not maxHeap:
                    return ""
                nextFreq, nextChar = heapq.heappop(maxHeap)
                res.append(nextChar)
                prevChar = nextChar
                if nextFreq+1<0:
                    heapq.heappush(maxHeap, (nextFreq+1, nextChar))
                heapq.heappush(maxHeap, (freq, char))

            else:
                 res.append(char)
                 prevChar = char
                 if freq+1<0:
                    heapq.heappush(maxHeap, (freq+1, char))
        return "".join(res)


    
            
# @lc code=end

