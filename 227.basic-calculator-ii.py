#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def __init__(self):
        # Define operator precedence
        self.map = {
            '-': 1,
            '+': 1,
            '*': 2,
            '/': 2,
            '%': 2,
            '^': 3
        }
    def calc(self, nums, ops):
        if len(nums) < 2 or not ops:
            return
        b = nums.pop()
        a = nums.pop()
        op = ops.pop()
        if op == '+':
            ans = a + b
        elif op == '-':
            ans = a - b
        elif op == '*':
            ans = a * b
        elif op == '/':
            ans = a // b  # Use integer division
        elif op == '^':
            ans = a ** b
        elif op == '%':
            ans = a % b
        nums.append(ans)

    def calculate(self, s: str) -> int:
        # Remove all spaces
        s = s.replace(" ", "")
        n = len(s)

        # Store all numbers
        nums = []
        # Store all operators
        ops=[]

        i = 0 
        while i < n:
            if s[i] =='(':
                ops.append(s[i])
            elif s[i] ==')':
                # need to find the matching (
                # and calculate between ( and )
                while ops and ops[-1]!='(':
                    self.calc(nums, ops)
                # we pop the most recent (
                ops.pop()
            else:
                # 此时char是数字
                if s[i].isdigit():
                    curNum = 0
                    j = i
                    # Extract the whole number starting from position i
                    while j < n and s[j].isdigit():
                        curNum = curNum * 10 + int(s[j])
                        j += 1
                    nums.append(curNum)
                    # 此时 j 不是数字
                    # 因为跳出这个循环我们还会i+1
                    # 避免重复我们 set i=j-1
                    i = j-1
                # 此时char不是数字
                else:
                    # if i > 0 and (s[i - 1] == '(' or s[i - 1] == '+' or s[i - 1] == '-'):
                    # nums.append(0)
                    # When a new operator is to be added, calculate the stack first if possible
                    # Only calculate when the operator on stack has higher or equal priority
                    while ops and ops[-1] != '(' and self.map[ops[-1]] >= self.map[s[i]]:
                        self.calc(nums, ops)
                    ops.append(s[i])
            i += 1
        
        # Calculate the remaining operators
        while ops:
            self.calc(nums, ops)
        return nums[-1]
                     
# @lc code=end

