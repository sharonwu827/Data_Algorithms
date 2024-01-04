#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#

# @lc code=start
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dict_1 = {}
        dict_2 = {}
        start = 0 
        for end_1 in range(start, len(nums1)):
            dict_1[nums1[end_1]] = dict_1.get(nums1[end_1], 0)+1
            for end_2 in range(start, len(nums2)):
                dict_2[nums2[end_2]] = dict_2.get(nums1[end_2], 0)+1
                if 


        
# @lc code=end

