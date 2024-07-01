#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # find the first val == x and the first val > x
        n = len(arr)

        def firstSmallerIndex(arr, x):
            left = 0 
            right = n-1
            while left<=right:
                mid = left+(right-left)//2
                if arr[mid]>=x:
                    right = mid-1
                else:
                    left = mid+1
            if left-1<0:
                return 0
            else:
                return left-1
        
        def firstLargerIndex(arr, x):
            left = 0 
            right = n-1
            while left<=right:
                mid = left+(right-left)//2
                if arr[mid]>x:
                    right = mid-1
                else:
                    left = mid+1
            return left
        
        leftInd = firstSmallerIndex(arr, x)
        # print(leftInd)
        rightInd = firstLargerIndex(arr, x)
        # print(rightInd)
        curLen = rightInd-leftInd+1
        # print(curLen)

        while curLen<k:
            if leftInd ==0:
                rightInd+=1
                continue
            if rightInd == n-1 or abs(arr[leftInd]-x)<=abs(arr[rightInd]-x):
                leftInd-=1     
            else:
                rightInd+=1
        return [leftInd, rightInd]       




    
# @lc code=end

