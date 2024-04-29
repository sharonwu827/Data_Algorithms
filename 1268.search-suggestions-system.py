#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#

# @lc code=start
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    
        res = []
        products.sort()
        for i in range(len(searchWord)):
            tmp = []
            for j in range(len(products)):
                if products[j][i] == searchWord[i] and len(tmp)<3:
                    tmp.append(products[j])
            res.append(tmp)
        return res

                

        
# @lc code=end

