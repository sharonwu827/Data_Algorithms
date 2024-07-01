#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        # 将最小值放在末端 to achieve O(1) when getMin()
        self.minStack.append(min(val, self.minStack[-1]))
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
         return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

