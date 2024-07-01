#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        curZero = 0 
        curLen = 0
        for right in range(len(nums)):
            if nums[right]==0:
                curZero+=1 
            while curZero>k:
                if nums[left]==0:
                    curZero-=1
                left+=1
            # we can update curLen without explicitly checking if curZero <= k 
            # because the while loop ensures that curZero > k is always false 
            # before the window size is updated
            curLen = max(curLen, right-left+1)
        return curLen
    

        
# @lc code=end

