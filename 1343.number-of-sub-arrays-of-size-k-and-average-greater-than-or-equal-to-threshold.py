#
# @lc app=leetcode id=1343 lang=python3
#
# [1343] Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#

# @lc code=start


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0 
        n = len(arr)
        start = 0 
        end = 0 
        target = k*threshold
        curSum = 0 
        for end in range(n):
            curSum+=arr[end]
            # 这两个if 不能更换位置
            if end-start+1 > k:
                curSum-=arr[start]
                start+=1
            if end-start+1==k and curSum>=target:
                res+=1
        return res
        
# @lc code=end

