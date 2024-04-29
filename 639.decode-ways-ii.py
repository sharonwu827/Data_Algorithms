#
# @lc app=leetcode id=639 lang=python3
#
# [639] Decode Ways II
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        
# @lc code=end

def sort(nums, low, high):
    if low >= high:
        return
    mid = (low+high)//2
    left = sort(nums, low, mid)
    right = sort(nums, mid+1, high)
    merge(left, right)

def mergeSort(self, left, right):
    """合并两个已排序好的列表，产生一个新的已排序好的列表"""
	result = []  # 新的已排序好的列表
	i = 0  # 下标
	j = 0
	# 对两个列表中的元素 两两对比。
	# 将最小的元素，放到result中，并对当前列表下标加1
	while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
			i += 1
		else:
            result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result



