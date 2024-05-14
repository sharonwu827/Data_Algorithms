#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        # must start with a single slash '/'.
        # Directories within the path should be separated by only one slash '/'
        # It should exclude any single or double periods used to denote current or parent directories.
        words = path.split("/")
        stack = []
        for word in words:
            if word == '..':
                # we need to remove the prev word
                if stack:
                    stack.pop()
            elif word and word != '.': #注意这个条件
                stack.append(word)
        res = '/' + ('/').join(stack)
        return res

                


        
# @lc code=end

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(curNode):
            if not curNode:
                return 
            dfs(curNode.left)
            if self.pre:
                self.pre.right, curNode.left = curNode, self.pre
            else:  #代表正在访问链表头节点
                self.head = curNode
            self.pre =  curNode
            dfs(curNode.right)
            
        if not root:
            return 
        self.pre = None
        dfs(root)
        self.head.left = self.pre 
        self.pre.right = self.head
        return self.head


        

