#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res = []
        while queue:
            curCnt = 0
            curSum = 0 
            for _ in range(len(queue)):
                curNode = queue.pop(0)
                curCnt +=1
                curSum += curNode.val
                if curNode.left:
                    queue.append(curNode.left)
                if curNode.right:
                    queue.append(curNode.right)
            res.append(curSum/curCnt)
        return res

        
        
# @lc code=end

