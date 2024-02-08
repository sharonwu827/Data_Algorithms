#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快指针：寻找新数组的元素 ，新数组就是不含有目标元素的数组
        # 慢指针：指向更新 新数组下标的位置
        slow = 0 
        fast = 1
        while fast<len(nums):
            if nums[slow] != nums[fast]:
                slow+=1
                nums[slow] = nums[fast]
            fast+=1
        return slow+1



# @lc code=end

