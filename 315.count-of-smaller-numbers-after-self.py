#
# @lc app=leetcode id=315 lang=python3
#
# [315] Count of Smaller Numbers After Self
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
# @lc code=end


def sort(nums: List[int], lo: int, hi: int):
    if lo >= hi:
        return
    # 对 nums[lo..hi] 进行切分
    # 使得 nums[lo..p-1] <= nums[p] < nums[p+1..hi]
    p = partition(nums, lo, hi)
    # 去左右子数组进行切分
    sort(nums, lo, p - 1)
    sort(nums, p + 1, hi)