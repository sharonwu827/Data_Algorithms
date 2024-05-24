#
# @lc app=leetcode id=2104 lang=python3
#
# [2104] Sum of Subarray Ranges
#

# @lc code=start
class Solution:
    def subArrayRanges(self, nums) -> int:
        n = len(nums)
        minLeft = [-1]*n  # 左侧最近的比它小的数的index
        maxLeft = [-1]*n  # 左侧最近的比它大或相等的数的index
        minRight =  [n]*n # 右侧最近的比它小的数的index 这里不能[-1]*n
        maxRight =  [n]*n # 右侧最近的比它大或相等的数的index 这里不能[-1]*n
        stack = []

        # 左侧最近的比它小的数的index
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i]<=nums[stack[-1]]:
                index = stack.pop()
                minLeft[index] = i
            stack.append(i)
        print (minLeft)

        # 左侧最近的比它大或相等的数的index
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[i]>nums[stack[-1]]:
                index = stack.pop()
                maxLeft[index] = i
            stack.append(i)
        print (maxLeft)

        # 右侧最近的比它小的数的index
        stack = []
        for i in range(n):
            while stack and nums[i]<nums[stack[-1]]:
                index = stack.pop()
                minRight[index] = i 
            stack.append(i)
        print (minRight)

        # 右侧最近的比它大或相等的数的index
        stack = []
        for i in range(n):
            while stack and nums[i]>=nums[stack[-1]]:
                index = stack.pop()
                maxRight[index] = i 
            stack.append(i)
        print (maxRight)

        # 计算每个元素对答案的贡献
        # 以此元素为最小值的子数组个数为(i - minLeft[i])×(minRight[i] - i)；
        # 以此元素为最大值的子数组个数为(i - maxLeft[i])×(maxRight[i] - i)。
        sumMax, sumMin = 0, 0
        for i, num in enumerate(nums):
            sumMax += (maxRight[i] - i) * (i - maxLeft[i]) * num
            sumMin += (minRight[i] - i) * (i - minLeft[i]) * num
        return sumMax - sumMin


    
solution = Solution();
testCase = [1,3,3]
print(solution.subArrayRanges(testCase))

        
        
    
            