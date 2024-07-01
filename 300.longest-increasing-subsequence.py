#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def getLastIndlarger(curNum, curInd):
            left = 0 
            right = curInd
            while left<right:
                mid = left+(right-left)//2
                if stack[mid]>=curNum: # 这里不是stack[mid]>curNum:
                    right = mid
                else:
                    left = mid+1
            return left

        stack = []
        for num in nums:
            if stack and stack[-1]<num or not stack:
                stack.append(num)
            else:
                # stack[-1]>=num
                # we cannot make longest increasting sub by appending the cur num
                # we need to find the last number that >= num -> can use binary search
                # we need to change that last number with current number
                LastIndlarger = getLastIndlarger(num, len(stack)-1)
                stack[LastIndlarger] = num
        return len(stack)

# @lc code=end

