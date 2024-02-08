#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 
        fast = 0 
        #快慢指针间隔的数就是num of element that = val
        while fast<len(nums):
            if fast<len(nums) and nums[fast]!=val:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1 
        return slow
    
# @lc code=end

