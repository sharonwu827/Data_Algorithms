#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums
        
        hashmap = {}
        heap = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0)+1

        def partition(nums, low, high):
            pivot = nums[low]
            i, j = low, high
            while i<j:
                while i<j and nums[j]>=pivot:
                    j-=1
                while i<j and nums[i]

        



        
# @lc code=end

