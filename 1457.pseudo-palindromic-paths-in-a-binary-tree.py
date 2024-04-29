#
# @lc app=leetcode id=1457 lang=python3
#
# [1457] Pseudo-Palindromic Paths in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isPalindrome(arr):
            if len(arr)%2 == 0:
                for i in arr:

                i
            else:

        
        self.res = 0
        self.curPath = []
        def traverse(node):
            if not node:
                return 
            self.curPath.append(node.val)
            if not node.left and not node.right:
                if isPalindrome(self.curPath):
                    self.res+=1
            traverse(node.left)
            traverse(node.right)
            self.curPath.pop()
        traverse(root)
        return self.res
            
        
# @lc code=end



class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.smallDiff = float("inf")
        self.curDiff = 0
        self.res = 0
        def traverse(node):
            if not node:
                return 
            self.curDiff = abs(node.val - target)
            if self.curDiff < self.smallDiff:
                self.smallDiff = self.curDiff
            if self.curDiff == self.smallDiff:
                self.res = min(node.val, self.res)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return self.res