#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # return the number of elements in nums which are not equal to val.
        left = 0 
        right = 0 # point to pos where val!=val
        while right <len(nums):
            if nums[right]==val:
                right+=1
            else:
                nums[left] = nums[right]
                left+=1
                right+=1
        return left

            



            
                    

                
                

        
# @lc code=end

