#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False
        queue = [root]
        while queue:
            cur_sum = 0
            for _ in range(len(queue)):
                cur = queue.pop(0)
                cur_sum+=cur.val
                if cur.left:
                    queue.append(cur.left)
                    cur_sum+=cur.left.val
                if cur.right:
                    queue.append(cur.right)
                    cur_sum+=cur.right.val
                if not cur.left and not cur.right and cur_sum+cur.val == targetSum:
                    return True
        return False
          
# @lc code=end

