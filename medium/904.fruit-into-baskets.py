#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # longest consective string that include max two differnt type
        start = 0 
        dict_={}
        max_len = 1 
        cur_len = 0 

        for end in range(start, len(fruits)):
            dict_[fruits[end]] = dict_.get(fruits[end], 0)+1
            
            while len(dict_)>2:
                dict_[fruits[start]] -= 1
                if not dict_[fruits[start]]:
                    del dict_[fruits[start]]
                start+=1
            max_len = max(end-start+1, max_len)
        return  max_len
    
# @lc code=end

