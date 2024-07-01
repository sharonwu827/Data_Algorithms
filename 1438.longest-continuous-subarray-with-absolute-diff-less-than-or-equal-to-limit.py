#
# @lc app=leetcode id=1438 lang=python3
#
# [1438] Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
#

# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        minStack = deque() # 单调递增
        maxStack =deque()  # 单调递减
        res = 0
        left=0

        for i in range(n):
            
            while minStack and nums[minStack[-1]] > nums[i]:
                minStack.pop()
            minStack.append(i)

            while maxStack and nums[maxStack[-1]] < nums[i]:
                 maxStack.pop()
            maxStack.append(i)

            while nums[maxStack[0]] - nums[minStack[0]] > limit:
                if minStack[0] ==left:
                    minStack.popleft()
                if maxStack[0]==left:
                    maxStack.popleft()
                left+=1

            res = max(res, i-left+1)
        return res


                   
# @lc code=end

