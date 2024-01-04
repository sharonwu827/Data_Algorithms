#
# @lc app=leetcode id=1095 lang=python3
#
# [1095] Find in Mountain Array
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findPeak(mountain_arr):
            left = 0 
            right = mountain_arr.length()-1
            while left<right:
                mid = left+(right-left)//2
                if mountain_arr.get(mid)>mountain_arr.get(mid+1):
                    # mid can be the peak
                    right = mid
                else:
                    left = mid+1
            return left # the peak index
        
        def findLeft(mountain_arr, left, right):
            while left <= right:
                mid = left+(right-left)//2
                if mountain_arr.get(mid)==target:
                    return mid
                elif mountain_arr.get(mid)>target:
                    # mid wont be equal to target, narrow the left array to end at mid-1
                    right = mid-1
                else:
                    left = mid+1
            return -1
        
        def findRight(mountain_arr,  left, right):
            while left<=right:
                mid = left+(right-left)//2
                if mountain_arr.get(mid)==target:
                    return mid
                elif mountain_arr.get(mid)<target:
                    right = mid-1
                else:
                    left = mid+1
            return -1

        
        peak = findPeak(mountain_arr)
        left = findLeft(mountain_arr, 0, peak)
        right = findRight(mountain_arr, peak, mountain_arr.length()-1)

        if left == -1 and right == -1:
            return -1
        else:
            return left if left!=-1 else right
     

    
# @lc code=end

