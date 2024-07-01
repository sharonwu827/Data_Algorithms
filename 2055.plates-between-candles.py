#
# @lc app=leetcode id=2055 lang=python3
#
# [2055] Plates Between Candles
#

# @lc code=start
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        preSum = [0] * (len(s)+1)  # presum: 统计*的前缀和
        for i in range(1, n+1):
            if s[i-1] == '*':
                preSum[i] = preSum[i-1] + 1
            else:
                preSum[i] = preSum[i-1]
        print(preSum)

        left = [-1] * len(s) # 统计每个坐标左边最近的|的坐标
        right = [-1] * len(s) # 统计每个坐标右边最近的|的坐标
        
        curInd = -1
        for i in range(n):
            if s[i]=='|':
                curInd=i
            left[i] = curInd
        print(left)

        curInd = -1
        for i in range(n-1, -1, -1):
            if s[i]=='|':
                curInd=i
            right[i] = curInd
        print(right)

        res = []
        for i, (l, r) in enumerate(queries):
            leftInd = right[l] 
            rightInd = left[r] 
            if leftInd!=-1 and rightInd!=-1 and leftInd<rightInd:
                res.append(preSum[rightInd] - preSum[leftInd])
            else:
                res.append(0)
        return res

            
        
        
  
    
# @lc code=end

