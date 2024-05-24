#
# @lc app=leetcode id=1856 lang=python3
#
# [1856] Maximum Subarray Min-Product
#

# @lc code=start
class Solution:
    def maxSumMinProduct(self, nums) -> int:
        n = len(nums)
        stack = []
        minLeft = [-1]*n
        minRight = [n]*n

        for i in range(n):
            while stack and nums[stack[-1]]>=nums[i]:
                index = stack.pop()
                minRight[index] = i
            if stack:
                minLeft[i] = stack[-1]
            stack.append(i)
        print(minLeft, minRight)
        # 利用前缀和的方式，可逐一当前元素及之前所有元素求和
        # 提取每个子数组的和时，可利用其左右边界从前缀和数组直接提取相减
        # preSum中的第i个元素，为nums的第i-1个元素左侧所有元素（包含自己）的累加和
        preSum = [0] 
        for num in nums:
            preSum.append(preSum[-1] + num)
        print(preSum)
        res = -float('inf') 
        for i in range(n):
            left = minLeft[i]
            right = minRight[i]
            print(left, right)
            # minimumVal in the array * sum of the array
            # 在这个 array with minimumVal, get the sum from nums[left+1] to nums[right-1]
            # nums[left+1:right] = preSum[right] - preSum[left+1] 
            cur = nums[i] * (preSum[right] - preSum[left+1]) 
            res = max(res, cur)
        return res % (10 ** 9 + 7)
    
solution = Solution();
testCase = [1,4,2,9,6]
print(solution.maxSumMinProduct(testCase))
        
# @lc code=end

