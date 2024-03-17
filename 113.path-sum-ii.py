#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.all_paths = []

        def dfs(node, current_sum, current_path):
            if not node:
                return

            current_sum += node.val
            current_path.append(node.val)

            if not node.left and not node.right and current_sum == targetSum:
                self.all_paths.append(list(current_path))

            dfs(node.left, current_sum, current_path)
            dfs(node.right, current_sum, current_path)

            current_sum -= node.val
            current_path.pop()

        if root:
            dfs(root, 0, [])

        return self.all_paths

    


            

        
# @lc code=end

