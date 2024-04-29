#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.hashset = set()
        self.res = []

        def treeSerialize(node):
            if not node:
                return "#"
            left = treeSerialize(node.left)
            right = treeSerialize(node.right)
            nodeSerialize = left + "," + right + "," + str(root.val)
            if nodeSerialize in self.hashset:
                self.res.append(root)
            else:
                self.hashset.add(nodeSerialize)
                
        treeSerialize(root)
        return self.res

            



        
# @lc code=end

