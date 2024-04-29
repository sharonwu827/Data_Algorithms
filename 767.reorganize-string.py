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
        if maxFreq>(len(s)+1)//2:
            return ''
        
        res = []
        while len(maxHeap)>=2:
            #当最大堆的元素个数大于 1 时，每次从最大堆取出两个字母，拼接到重构的字符串，
            freq1, char1 = heapq.heappop(maxHeap)
            freq2, char2 = heapq.heappop(maxHeap)
            res.append(char1)
            res.append(char2)
            # 将两个字母的出现次数分别减 1，并将剩余出现次数大于 0 的字母重新加入最大堆
            if -freq1>1:
                heapq.heappush(maxHeap,  (freq1+1, char1))
            if -freq2>1:
                heapq.heappush(maxHeap,  (freq2+1, char2))
        
        if maxHeap:
            res.append(maxHeap[0][1])
        
        return ''.join(res)
            
# @lc code=end

