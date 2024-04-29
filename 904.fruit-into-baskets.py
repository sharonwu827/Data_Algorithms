#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0 
        right = 0 
        dict_= {}
        res = 0 
        for right in range(len(fruits)):
            treeType = fruits[right]
            dict_[treeType] = dict_.get(treeType, 0)+1
            
            while len(dict_)>2:
                dict_[fruits[left]]-=1
                if not dict_[fruits[left]]:
                    del dict_[fruits[left]]
                left+=1
            res = max(res, right-left+1)
        return res
            
        

            
        
# @lc code=end

