#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def getCombination(i):
            if nums[i]>0:
                return 
            left = i+1
            right= len(nums)-1
            
            res = []
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total == 0:
                    res.append([nums[i],nums[left],nums[right]])
                    #注意什么时候去重
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1 
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
            return res
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            while i>0 and nums[i]==nums[i-1]:
                i+=1
            if getCombination(i):
                res.extend(getCombination(i))
        return res

