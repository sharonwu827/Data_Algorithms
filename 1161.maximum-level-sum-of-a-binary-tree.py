#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        maxSum = -float("inf")
        level = 1
        maxLevel = 0
        while queue:
            curSum = 0 
            for _ in range(len(queue)):
                curNode = queue.pop(0) # Pop from the left side of the queue (FIFO)
                curSum+=curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            if maxSum < curSum:
                maxLevel = level
                maxSum = curSum
            level+=1
        return maxLevel
        
# @lc code=end

