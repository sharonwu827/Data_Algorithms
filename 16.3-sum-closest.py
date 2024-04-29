#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=startfrom typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        min_diff = float("inf")
        for i in range(len(nums)-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]==target:
                    res = target
                    return res
                elif nums[i]+nums[left]+nums[right]>target:
                    if abs(nums[i]+nums[left]+nums[right]-target)<min_diff:
                        res = nums[i]+nums[left]+nums[right]
                        min_diff = abs(nums[i]+nums[left]+nums[right]-target)
                    right-=1
                else:
                    if abs(nums[i]+nums[left]+nums[right]-target)<min_diff:
                        res = nums[i]+nums[left]+nums[right]
                        min_diff = abs(nums[i]+nums[left]+nums[right]-target)
                    left+=1
        return res


       
# @lc code=end

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        self.res = 0
        def dfs(startInd, path):
            if len(path)==3 and sum(path)<target:
                self.res+=1
                return
            if sum(path)>=target or len(path)>3:
                return 
            for i in range(startInd, len(nums)):
                if i>startInd and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
        dfs(0, [])
        return self.res

            
        