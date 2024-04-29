#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
        return res
        
# @lc code=end

