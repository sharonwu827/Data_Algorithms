#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # store index
        nextGreater = [-1] * len(nums1)
    
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                if nums2[stack[-1]] in nums1: 
                    nums1Index = nums1.index(nums2[stack[-1]])
                    nextGreater[nums1Index] = nums2[i]
                    stack.pop()
                else:
                    stack.pop()
            stack.append(i)
        return nextGreater


        
        
# @lc code=end

