#
# @lc app=leetcode id=987 lang=python3
#
# [987] Vertical Order Traversal of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append((root, 0, 0))
        columnTable = defaultdict(list)
        while queue:
            cur, column, row = queue.popleft()
            columnTable[column].append((cur.val,row))
            if cur.left:
                queue.append((cur.left, column-1, row+1))
            if cur.right:
                queue.append((cur.right, column+1, row+1))
        
        res = []
        # sort the table based on the ascending order of column
        for col in sorted(columnTable.keys()):
            # sorting the list of tuples based on the row 
            columnTable[col].sort(key=lambda x:(x[1], x[0]))
            column_values = []
            for val, _ in columnTable[col]:
                column_values.append(val)
            res.append(column_values)
        return res

                  
# @lc code=end

