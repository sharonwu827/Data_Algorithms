#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def sort(left, right):
            res = []
            i = 0 
            j = 0 
            while i<len(left) and j <len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i+=1
                else:
                    res.append(right[j])
                    j+=1
            if i<len(left):
                res.append(left[i:])
            if j<len(right):
                res.append(right[j:])
            return res
        
        for i in 



        
# @lc code=end

