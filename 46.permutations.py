#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        used = [False]*len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
           
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] =False
        backtrack([])
        return res
        
        
# @lc code=end

