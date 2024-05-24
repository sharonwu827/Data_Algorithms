#
# @lc app=leetcode id=2281 lang=python3
#
# [2281] Sum of Total Strength of Wizards
#

# @lc code=start
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        stack = []
        minLeft = [-1]*n
        minRight = [n]*n

        for i in range(n):
            while stack and strength[stack[-1]]>=strength[i]:
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
        for num in strength:
            preSum.append(preSum[-1] + num)
        print(preSum)
        res = 0
        for i in range(n):
            left = minLeft[i]
            right = minRight[i]
            # print(left, right)
            # minimumVal in the array * sum of the array
            # 在这个 array with minimumVal, get the sum from nums[left+1] to nums[right-1]
            # nums[left+1:right] = preSum[right] - preSum[left+1] 
            
            # Get the left_count and right_count 
            leftCount = i - left
            rightCount = right - i
            mod = 10 ** 9 + 7
            neg_presum = (preSum[i + 1] - preSum[i - leftCount + 1]) % mod
            pos_presum = (preSum[i + rightCount + 1] - preSum[i + 1]) % mod
            print(i, cur)
            res += cur
        return res 
    
solution = Solution();
testCase = [1,3,1,2]
print(solution.totalStrength(testCase))
        
# @lc code=end

