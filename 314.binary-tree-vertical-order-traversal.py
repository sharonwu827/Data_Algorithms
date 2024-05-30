#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        dict_ = defaultdict(list) 
        queue = deque()
        queue.append((root, 0, 0))
        
        while queue:
            cur, x, y = queue.popleft()
            dict_[x].append((y, cur.val))
            if cur.left:
                queue.append( (cur.left, x-1, y+1))
            if cur.right:
                queue.append( (cur.right, x+1, y+1))
        
        res = []
        for x in sorted(dict_.keys()):
            dict_[x].sort(key = lambda x:x[0])
            temp = []
            for _, val in dict_[x]:
                temp.append(val)
            res.append(temp)
        return res
       
# @lc code=end

