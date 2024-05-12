#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums.sort() # O(nlogN)
        # 2. hashtable
        hashTable = Counter(nums)
        for val in hashTable.values():
            if val>1:
                return True
        return False
    
        
# @lc code=end

