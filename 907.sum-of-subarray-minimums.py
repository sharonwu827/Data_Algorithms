#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        minLeft = [-1] * n
        minRight = [n] * n

        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]>arr[i]:
                minLeft[stack[-1]] = i
                stack.pop()
            stack.append(i)
        print(minLeft)
        stack.clear()
         # for deal with duplicate value
         # find the right element which smaller than or equal to nums[i]
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                minRight[stack[-1]] = i
                stack.pop()
            stack.append(i)
        print(minRight)
        
        res = 0
        for i in range(n):
            res+= arr[i] * (i-minLeft[i]) * (minRight[i]-i)
        # Since the answer may be large, return the answer modulo 109 + 7.
        return res % (10 ** 9 + 7)


            
