#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[] #O(N)
        indexToRemove = set() #o(n)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append((s[i], i))
            if s[i] == ')':
                if not stack:
                    indexToRemove.add(i)
                else:
                    stack.pop()
        if stack:
            for val, index in stack:
                indexToRemove.add(index)
        
        res = []
        for i in range(len(s)):
            if i not in indexToRemove:
                res.append(s[i])
        return ''.join(res)

Solution = Solution
testCase1 = "lee(t(c)o)de)"
res = Solution.minRemoveToMakeValid(testCase1)
print(res)



class Solution:
    def calculate(self, s: str) -> int:
        hashmap = {'-':1, '+': 1, '*':2, '/':2, '%':2, '^':3}
        stack = []
        i = 0 
        curNumber = deque([0])
        preOperation = deque() # 记录每个数字之前的运算符

        def helper(nums, operation):
            if not nums or len(nums)<2 or not opeartion:
                return 
            b, a = nums.pop(), nums.pop()
            opeartion = operation.pop()
            res = 0 
            if operation == '+':
                res = a + b
            elif operation =='-':
                res = a - b
            elif preOperation=='*':
                res = b * a
            elif preOperation=='/':
                res = a // b
            elif preOperation=='^':
                res = a^b
            nums.append(res)

        while i<len(s):
            if s[i].isdigit():
                num = 

            elif s[i] == '(':
                preOperation.append(s[i])
            elif s[i] == ')':
                while preOperation[-1] != '(':
                    self.helper(nums, preOperation)
                preOperation.pop()  # 弹出左括号
            
            

    
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prevHigest = -float('inf')
        res = []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > prevHigest:
                res.append(i)
                prevHigest = heights[i]
        return res[::-1]
            


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(strength)
        
        # Get the first index of the non-larger value to strength[i]'s right.
        right_index = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right_index[stack.pop()] = i
            stack.append(i)

        # Get the first index of the smaller value to strength[i]'s left.
        left_index = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left_index[stack.pop()] = i
            stack.append(i)
            
        # prefix sum of the prefix sum array of strength.
        presum_of_presum =  list(accumulate(accumulate(strength, initial = 0), initial = 0))
        answer = 0
        # For each element in strength, we get the value of R_term - L_term.
        for i in range(n):
            # Get the left index and the right index.
            left_bound = left_index[i]
            right_bound = right_index[i]
            
            # Get the left_count and right_count (marked as L and R in the previous slides)
            left_count = i - left_bound
            right_count = right_bound - i
            
            # Get positive presum and the negative presum.
            neg_presum = (presum_of_presum[i + 1] - presum_of_presum[i - left_count + 1]) % mod
            pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod
            
            # The total strength of all subarrays that have strength[i] as the minimum.
            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            answer %= mod
            
        return answer
    


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        mod = 10 ** 9 + 7
        # 1. 对于每个数组元素 a[i]，首先求出两个数组
        # left[i] 为左侧严格小于 strength[i] 的最近元素位置（不存在时为 -1）
        # right[i] 为右侧小于等于 strength[i] 的最近元素位置（不存在时为 n）
        leftFirstSmaller = [-1] * n
        rightFirstSmaller = [n] * n
        # Get the first index of the smaller value to strength[i]'s left.
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]]>=strength[i]:
                index = stack.pop()
                leftFirstSmaller[index]=i
            stack.append(i)
        # Get the first index of the non-larger value to strength[i]'s right.
        stack = []
        for j in range(n):
            while stack and strength[stack[-1]]>strength[i]:
                index = stack.pop()
                rightFirstSmaller[index]=i
            stack.append(i)
        # print( leftFirstSmaller, rightFirstSmaller )
        # 2. prefix sum of the prefix sum array of strength.
        presum_of_presum =  list(accumulate(accumulate(strength, initial = 0), initial = 0))
        # print( presum_of_presum )
        res = 0
        # 3. For each element in strength, we get the value of R_term - L_term.
        for i in range(n):
            left_bound = leftFirstSmaller[i]
            right_bound = rightFirstSmaller[i]

            left_count = i - left_bound
            right_count = right_bound - i

            neg_presum = (presum_of_presum[i + 1] - presum_of_presum[i - left_count + 1]) % mod
            pos_presum = (presum_of_presum[i + right_count + 1] - presum_of_presum[i + 1]) % mod
            
            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            answer %= mod
        return res
            





class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        n = len(nums2)
        res = [n]*n
        for i in range(n):
            while stack and nums2[i]<nums2[stack[-1]]:
                index = stack.pop()
                res[i] = index
            stack.append(i)
        


                