#
# @lc app=leetcode id=528 lang=python3
#
# [528] Random Pick with Weight
#

# @lc code=start
class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.preSum = [0]*n
        self.preSum[0] = w[0]
        # 前缀和
        for i in range(1, n):
            self.preSum[i] = self.preSum[i-1] + w[i]

        #  # 计算前缀和，这样可以生成一个随机数，根据数的大小对应分布的坐标
        # self.presum = list(accumulate(w))

    def pickIndex(self) -> int:
        seed = random.randint(1, self.preSum[-1])
        index = bisect_left(self.preSum, seed)
        return index
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

