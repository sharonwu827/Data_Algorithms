#
# @lc app=leetcode id=852 lang=python3
#
# [852] Peak Index in a Mountain Array
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr)-2
        while left<right:
            mid = left+(right-left)//2
            if arr[mid]>arr[mid+1]:
                right = mid
            else:
                left = mid+1
        return left
# @lc code=end

