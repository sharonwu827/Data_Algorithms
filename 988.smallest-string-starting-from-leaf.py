#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.path = []
        self.res = None
        self.traverse(root)
        return self.res

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.path.append(chr(ord('a') + root.val))
        if not root.left and not root.right:
            modifiedPath = "".join(self.path[::-1])
            if not self.res or self.res > modifiedPath:
                # 如果字典序更小，则更新 res
                self.res = modifiedPath
            # 恢复，正确维护 path 中的元素
            self.path.pop()
            return
        self.traverse(root.left)
        self.traverse(root.right)
        self.path.pop()
                    
        
# @lc code=end

