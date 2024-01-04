#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # stack store nums2 ​中每个元素右边的第一个更大的值
        # 单调栈中维护当前位置右边的更大的元素列表，从栈底到栈顶的元素是单调递减的
        stack = []
        dict_ = {}
        for num in nums2:
            while stack and num >= stack[-1]:
                small = stack.pop()
                dict_[small] = num
            stack.append(num)
        return stack
        
nums1=[4,1,2]
num2=[1,3,4,2]
Solution()

# @lc code=end

