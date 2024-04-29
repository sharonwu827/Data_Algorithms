#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.preSum = [0]*(n+1)
        for i in range(n):
            self.preSum[i+1] = nums[i]+self.preSum[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.preSum[right+1]-self.preSum[left]

  

    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end

