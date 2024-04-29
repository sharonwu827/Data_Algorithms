#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        # any leaf node is equal to the avg of sum subtree
        self.res = 0
        # return sum of subtree and cnt
        def dfs(root):
            if not root:
                return 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            cnt = left[1]+right[1]+1
            curSum = left[0]+right[0]+root.val
            if curSum//cnt == root.val:
                self.res+=1
            return curSum, cnt
        dfs(root)
        return self.res
class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        left = 0 
        right = 0 
        dict2 = defaultdict(int)
        for char in s2:
            dict2[char] += 1
        
        dict1 = defaultdict(int)
        found = 0 
        min_len = float('inf')
        startInd = 0

        for right in range(len(s1)):
            char = s1[right]
            dict1[char]+=1
            if char in dict2 and dict1[char]==dict2[char]:
                found+=1
            # the current window meet requirement
            # move left pointer to find min window
            while found==len(dict2):
                if min_len>right-left+1:
                    startInd = left
                    min_len = right-left+1

                dict1[s1[left]]-=1
                if s1[left] in dict2 and dict1[s1[left]] < dict2[s1[left]]:
                    found-=1
                left+=1
        return s1[startInd:startInd+min_len]

                
            
