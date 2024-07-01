#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        target = (len(nums1)+len(nums2))//2
        l1 = len(nums1)
        l2 = len(nums2)
        p1 = 0 
        p2 = 0 
        flag = False #标记中间数取的是否为nums1的元素
        k = (m + n + 1) // 2    # 获取中间数是第几个数（偶数取前一个数）
        while True:
            # 数组1元素全部取完，剩下的元素由数组2提供
            if p1 == len(nums1):
                # [p2, ?]提供k个元素，即?-idx2+1=k => ? = idx2+k-1
                p2 += k-1
                break
            if p2 == len(nums2):
                p1 += k-1
                flag = True
                break
            if k ==1:
                flag = nums1[p1] < nums2[p2]   # 指针无需移动，只需要判断取哪个数组的元素
                break
            half = k//2
            mid1 = mid
