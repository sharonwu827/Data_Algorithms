#
# @lc app=leetcode id=907 lang=python3
#
# [907] Sum of Subarray Minimums
#

# @lc code=start
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        minLeft = [-1]*n
        minRight = [n]*n

        stack = []
        res = 0
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                index = stack.pop()
                minRight[index] = i
            # 此时所有>=arr[i]的index都出了stack
            # 剩下的就是arr[i]左侧最近的小元素
            if stack:
                minLeft[i]=stack[-1]
            res+= (i-minLeft[i])*(minRight[i]-i) * arr[i]
            stack.append(i)
        return res % (10 ** 9 + 7)

             
# @lc code=end

