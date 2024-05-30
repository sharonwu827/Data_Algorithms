#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
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

    def calculate(self, s: str) -> int:
        # Remove all spaces
        s = s.replace(" ", "")
        n = len(s)

        # list store all numbers
        nums = []
        # To prevent the first number from being negative, add a 0 first
        nums.append(0)
        # Store all operators
        ops = []

        i = 0
        while i < n:
            curChar = s[i]
            if curChar == '(':
                # 直接加入 ops 中，等待与之匹配的 )
                ops.append(curChar)
            elif curChar == ')':
                 # need to find the matching (
                # and calculate between ( and )
                while ops and ops[-1] != '(':
                    self.calc(nums, ops)
                ops.pop()
            
            else:
                 # 1. 此时char是数字
                if curChar.isdigit():
                    curNum = 0
                    j = i
                    # Extract the whole number starting from position i
                    while j < n and s[j].isdigit():
                        curNum = curNum * 10 + int(s[j])
                        j += 1
                    nums.append(curNum)
                    i = j - 1
                # 2. 此时char不是数字
                else:
                    if i > 0 and (s[i - 1] == '(' or s[i - 1] == '+' or s[i - 1] == '-'):
                        nums.append(0)
                    # When a new operator is to be added, calculate the stack first if possible
                    # Only calculate when the operator on the stack has higher or equal precedence
                    while ops and ops[-1] != '(' and self.map[ops[-1]] >= self.map[curChar]:
                        self.calc(nums, ops)
                    ops.append(curChar)
            i += 1
        # Calculate the remaining operators
        while ops:
            self.calc(nums, ops)
        return nums[-1]

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


        
# @lc code=end

